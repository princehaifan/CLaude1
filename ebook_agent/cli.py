"""Command-line entry point for the eBook agent pipeline.

Usage:
    python -m ebook_agent build --manuscript book.md --author "Jane Doe" \
        --subtitle "A practical guide" --price 9 --out dist/

    python -m ebook_agent cover --title "My Book" --author "Jane Doe" \
        --subtitle "Sub" --out dist/cover.png

The `build` command produces, in the output directory:
    cover.png, <slug>.pdf, <slug>.epub, <slug>.html, sales_kit.md, sales_kit.json
"""

from __future__ import annotations

import argparse
import json
import os
import sys

from .builder import BookMeta, build_epub, build_html_preview, build_pdf, parse_manuscript
from .cover import CoverSpec, generate_cover
from .sales import SalesInput, build_sales_kit, write_sales_kit


def _slug(s: str) -> str:
    return "".join(c if c.isalnum() else "-" for c in s.lower()).strip("-") or "book"


def cmd_build(args):
    with open(args.manuscript, encoding="utf-8") as fh:
        text = fh.read()

    title, chapters = parse_manuscript(text)
    title = args.title or title or "Untitled"
    if not chapters:
        print("error: no '## Chapter' sections found in manuscript", file=sys.stderr)
        return 2

    os.makedirs(args.out, exist_ok=True)
    slug = _slug(title)
    meta = BookMeta(title=title, author=args.author or "Anonymous",
                    subtitle=args.subtitle or "")

    # 1. Cover
    cover_path = os.path.join(args.out, "cover.png")
    generate_cover(CoverSpec(title=title, author=meta.author,
                             subtitle=meta.subtitle, badge=args.badge or ""),
                   cover_path)

    # 2. Formats
    pdf_path = build_pdf(meta, chapters, os.path.join(args.out, f"{slug}.pdf"), cover_path)
    epub_path = build_epub(meta, chapters, os.path.join(args.out, f"{slug}.epub"), cover_path)
    html_path = build_html_preview(meta, chapters, os.path.join(args.out, f"{slug}.html"))

    # 3. Sales kit
    words = sum(len(b.split()) for _, b in chapters)
    pages = max(1, words // 250)
    benefits = _read_list(args.benefits)
    hooks = _read_list(args.hooks)
    kit = build_sales_kit(SalesInput(
        title=title, author=meta.author, subtitle=meta.subtitle,
        audience=args.audience or "readers who want practical results fast",
        benefits=benefits, hooks=hooks, price=args.price, pages=pages))
    sales_path = write_sales_kit(kit, args.out)

    summary = {
        "title": title,
        "author": meta.author,
        "chapters": len(chapters),
        "word_count": words,
        "est_pages": pages,
        "outputs": {
            "cover": cover_path, "pdf": pdf_path, "epub": epub_path,
            "html_preview": html_path, "sales_kit": sales_path,
        },
        "suggested_price_usd": kit["pricing"]["standard"],
    }
    print(json.dumps(summary, indent=2))
    return 0


def cmd_cover(args):
    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    generate_cover(CoverSpec(title=args.title, author=args.author or "",
                             subtitle=args.subtitle or "", badge=args.badge or ""),
                   args.out)
    print(args.out)
    return 0


def cmd_sales(args):
    kit = build_sales_kit(SalesInput(
        title=args.title, author=args.author or "Anonymous",
        subtitle=args.subtitle or "", price=args.price,
        benefits=_read_list(args.benefits), hooks=_read_list(args.hooks)))
    os.makedirs(args.out, exist_ok=True)
    path = write_sales_kit(kit, args.out)
    print(path)
    return 0


def _read_list(val):
    if not val:
        return []
    if os.path.exists(val):
        with open(val) as fh:
            return [ln.strip("-• \n") for ln in fh if ln.strip()]
    return [x.strip() for x in val.split("|") if x.strip()]


def build_parser():
    p = argparse.ArgumentParser(prog="ebook_agent",
                                description="Create and package a sellable eBook.")
    sub = p.add_subparsers(dest="cmd", required=True)

    b = sub.add_parser("build", help="full pipeline: cover + PDF + EPUB + sales kit")
    b.add_argument("--manuscript", required=True, help="path to markdown manuscript")
    b.add_argument("--title", default="")
    b.add_argument("--author", default="")
    b.add_argument("--subtitle", default="")
    b.add_argument("--badge", default="")
    b.add_argument("--audience", default="")
    b.add_argument("--benefits", default="", help="'a|b|c' or a path to a file")
    b.add_argument("--hooks", default="", help="'a|b' or a path to a file")
    b.add_argument("--price", type=float, default=0.0)
    b.add_argument("--out", default="dist")
    b.set_defaults(func=cmd_build)

    c = sub.add_parser("cover", help="generate only a cover image")
    c.add_argument("--title", required=True)
    c.add_argument("--author", default="")
    c.add_argument("--subtitle", default="")
    c.add_argument("--badge", default="")
    c.add_argument("--out", default="dist/cover.png")
    c.set_defaults(func=cmd_cover)

    s = sub.add_parser("sales", help="generate only the sales/listing kit")
    s.add_argument("--title", required=True)
    s.add_argument("--author", default="")
    s.add_argument("--subtitle", default="")
    s.add_argument("--benefits", default="")
    s.add_argument("--hooks", default="")
    s.add_argument("--price", type=float, default=0.0)
    s.add_argument("--out", default="dist")
    s.set_defaults(func=cmd_sales)
    return p


def main(argv=None):
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
