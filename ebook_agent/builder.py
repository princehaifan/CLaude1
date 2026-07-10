"""Assemble a written manuscript into distributable eBook formats.

Input: a Markdown manuscript. Convention:
    # Book Title            -> book title (first H1)
    ## Chapter Title        -> a chapter / section
    ### Subheading          -> sub-section
    normal paragraphs, **bold**, *italic*, - bullets, 1. numbered, > quotes

Output: a print-ready PDF, a reflowable EPUB, and a styled HTML preview.
Only fpdf2, markdown, and ebooklib are required.
"""

from __future__ import annotations

import os
import re
from dataclasses import dataclass

import markdown as md
from ebooklib import epub
from fpdf import FPDF
from fpdf.enums import XPos, YPos

_NL = dict(new_x=XPos.LMARGIN, new_y=YPos.NEXT)


@dataclass
class BookMeta:
    title: str
    author: str
    subtitle: str = ""
    language: str = "en"


def parse_manuscript(text: str):
    """Split markdown into (title, [(chapter_title, chapter_md), ...])."""
    lines = text.splitlines()
    title = ""
    chapters = []
    current_title = None
    buf = []

    def flush():
        if current_title is not None:
            chapters.append((current_title, "\n".join(buf).strip()))

    for line in lines:
        if line.startswith("# ") and not line.startswith("## "):
            if not title:
                title = line[2:].strip()
                continue
        if line.startswith("## "):
            flush()
            current_title = line[3:].strip()
            buf = []
        else:
            buf.append(line)
    flush()

    # Content before the first chapter (front matter) becomes an intro chapter.
    if chapters and chapters[0][0] is None:
        chapters[0] = ("Introduction", chapters[0][1])
    return title, chapters


# ---------------------------------------------------------------- PDF --------
class _PDF(FPDF):
    def __init__(self, meta: BookMeta):
        super().__init__(format="A5")
        self.meta_title = meta.title
        self.meta_author = meta.author
        self.set_auto_page_break(auto=True, margin=18)
        self.set_margins(18, 20, 18)

    def footer(self):
        if self.page_no() <= 1:
            return
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(140, 140, 140)
        self.cell(0, 10, str(self.page_no()), align="C")


_MD_INLINE = re.compile(r"\*\*(.+?)\*\*|\*(.+?)\*|`(.+?)`")


# Map common Unicode punctuation to latin-1 so the core PDF fonts can render it.
_PUNCT = {
    "•": "·", "—": "-", "–": "-", "‘": "'",
    "’": "'", "“": '"', "”": '"', "…": "...",
    " ": " ", "→": "->",
}


def _clean(text: str) -> str:
    # Strip inline markdown emphasis for the PDF text layer (fpdf core fonts).
    text = _MD_INLINE.sub(lambda m: m.group(1) or m.group(2) or m.group(3), text)
    for k, v in _PUNCT.items():
        text = text.replace(k, v)
    return text.encode("latin-1", "replace").decode("latin-1")


def _render_pdf_chapter(pdf: _PDF, title: str, body_md: str):
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 22)
    pdf.set_text_color(20, 20, 40)
    pdf.multi_cell(0, 12, _clean(title), **_NL)
    pdf.ln(4)
    pdf.set_draw_color(200, 200, 210)
    pdf.line(pdf.l_margin, pdf.get_y(), pdf.w - pdf.r_margin, pdf.get_y())
    pdf.ln(6)

    for raw in body_md.split("\n"):
        line = raw.rstrip()
        if not line:
            pdf.ln(3)
            continue
        if line.startswith("### "):
            pdf.set_font("Helvetica", "B", 14)
            pdf.set_text_color(40, 40, 60)
            pdf.multi_cell(0, 8, _clean(line[4:]), **_NL)
            pdf.ln(1)
        elif re.match(r"^\s*[-*]\s+", line):
            pdf.set_font("Helvetica", "", 11)
            pdf.set_text_color(30, 30, 30)
            pdf.multi_cell(0, 7, _clean("  • " + re.sub(r"^\s*[-*]\s+", "", line)), **_NL)
        elif re.match(r"^\s*\d+\.\s+", line):
            pdf.set_font("Helvetica", "", 11)
            pdf.set_text_color(30, 30, 30)
            pdf.multi_cell(0, 7, "  " + _clean(line.strip()), **_NL)
        elif line.startswith("> "):
            pdf.set_font("Helvetica", "I", 11)
            pdf.set_text_color(90, 90, 110)
            pdf.multi_cell(0, 7, _clean(line[2:]), **_NL)
        else:
            pdf.set_font("Helvetica", "", 11)
            pdf.set_text_color(25, 25, 25)
            pdf.multi_cell(0, 7, _clean(line), **_NL)


def build_pdf(meta: BookMeta, chapters, out_path: str, cover_path: str | None = None):
    pdf = _PDF(meta)
    # Cover page.
    pdf.add_page()
    if cover_path and os.path.exists(cover_path):
        pdf.image(cover_path, x=0, y=0, w=pdf.w, h=pdf.h)
    else:
        pdf.ln(60)
        pdf.set_font("Helvetica", "B", 26)
        pdf.multi_cell(0, 14, _clean(meta.title), align="C", **_NL)
        if meta.subtitle:
            pdf.set_font("Helvetica", "I", 14)
            pdf.multi_cell(0, 10, _clean(meta.subtitle), align="C", **_NL)
        pdf.ln(20)
        pdf.set_font("Helvetica", "", 14)
        pdf.multi_cell(0, 10, _clean(meta.author), align="C", **_NL)

    # Table of contents.
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 20)
    pdf.set_text_color(20, 20, 40)
    pdf.multi_cell(0, 12, "Contents", **_NL)
    pdf.ln(4)
    pdf.set_font("Helvetica", "", 12)
    pdf.set_text_color(40, 40, 40)
    for i, (ct, _) in enumerate(chapters, 1):
        pdf.multi_cell(0, 8, _clean(f"{i}.  {ct}"), **_NL)

    for ct, body in chapters:
        _render_pdf_chapter(pdf, ct, body)

    pdf.output(out_path)
    return out_path


# --------------------------------------------------------------- EPUB --------
def build_epub(meta: BookMeta, chapters, out_path: str, cover_path: str | None = None):
    book = epub.EpubBook()
    book.set_identifier(re.sub(r"\W+", "-", meta.title.lower()).strip("-"))
    book.set_title(meta.title)
    book.set_language(meta.language)
    book.add_author(meta.author)

    if cover_path and os.path.exists(cover_path):
        with open(cover_path, "rb") as fh:
            book.set_cover("cover.png", fh.read())

    css = epub.EpubItem(
        uid="style", file_name="style/main.css", media_type="text/css",
        content=(
            "body{font-family:Georgia,serif;line-height:1.6;margin:5%;}"
            "h1{font-size:1.8em;border-bottom:2px solid #eee;padding-bottom:.3em;}"
            "h2{font-size:1.3em;color:#333;} blockquote{color:#555;"
            "border-left:3px solid #ddd;padding-left:1em;font-style:italic;}"
        ).encode(),
    )
    book.add_item(css)

    epub_chapters = []
    for i, (ct, body) in enumerate(chapters, 1):
        html_body = md.markdown(body, extensions=["extra", "sane_lists"])
        ch = epub.EpubHtml(title=ct, file_name=f"chap_{i}.xhtml", lang=meta.language)
        ch.content = f"<h1>{_html_escape(ct)}</h1>{html_body}".encode()
        ch.add_item(css)
        book.add_item(ch)
        epub_chapters.append(ch)

    book.toc = tuple(epub_chapters)
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())
    book.spine = ["nav"] + epub_chapters
    epub.write_epub(out_path, book)
    return out_path


def _html_escape(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


# --------------------------------------------------------------- HTML --------
def build_html_preview(meta: BookMeta, chapters, out_path: str):
    parts = [
        "<!doctype html><meta charset='utf-8'>",
        f"<title>{_html_escape(meta.title)}</title>",
        "<style>body{font-family:Georgia,serif;max-width:740px;margin:40px auto;"
        "line-height:1.65;color:#222;padding:0 20px;}h1{border-bottom:2px solid #eee;}"
        "h2{margin-top:2.5em;color:#1a1a2e;}blockquote{border-left:3px solid #ddd;"
        "color:#555;padding-left:1em;font-style:italic;}</style>",
        f"<h1>{_html_escape(meta.title)}</h1>",
    ]
    if meta.subtitle:
        parts.append(f"<p><em>{_html_escape(meta.subtitle)}</em></p>")
    parts.append(f"<p><strong>{_html_escape(meta.author)}</strong></p><hr>")
    for ct, body in chapters:
        parts.append(f"<h2>{_html_escape(ct)}</h2>")
        parts.append(md.markdown(body, extensions=["extra", "sane_lists"]))
    with open(out_path, "w") as fh:
        fh.write("\n".join(parts))
    return out_path
