"""Generate the assets you need to actually SELL the eBook.

Produces a ready-to-paste sales/listing kit: a Gumroad / Amazon KDP style
product description, pricing suggestions, keyword/category ideas, a launch
email, and social captions. The prose is templated; the agent (Claude) is
expected to enrich the `hooks`/`benefits` it passes in.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field


@dataclass
class SalesInput:
    title: str
    author: str
    subtitle: str = ""
    audience: str = "readers who want practical results fast"
    benefits: list = field(default_factory=list)   # bullet outcomes
    hooks: list = field(default_factory=list)       # one-liner hooks
    price: float = 9.0
    pages: int = 0


def suggest_pricing(pages: int, base: float) -> dict:
    """Simple pricing tiers around a base price."""
    if base <= 0:
        base = max(4.99, min(19.99, 3 + pages * 0.15))
    return {
        "launch": round(base * 0.6, 2),
        "standard": round(base, 2),
        "premium_bundle": round(base * 2.2, 2),
        "note": "Launch low for 48h to gather reviews, then raise to standard. "
                "Bundle = eBook + worksheets/templates for the premium tier.",
    }


def build_sales_kit(s: SalesInput) -> dict:
    benefits = s.benefits or [
        "A clear, step-by-step system you can start using today",
        "No fluff — every chapter ends with an action step",
        "Templates and examples you can copy",
    ]
    hooks = s.hooks or [
        f"Everything you need to master {s.title.lower()} — without the overwhelm.",
    ]
    pricing = suggest_pricing(s.pages, s.price)

    description = _description(s, benefits, hooks, pricing)
    launch_email = _launch_email(s, benefits)
    socials = _socials(s, hooks)
    listing = {
        "title": s.title,
        "subtitle": s.subtitle,
        "author": s.author,
        "suggested_price_usd": pricing["standard"],
        "categories": _categories(s),
        "keywords": _keywords(s),
    }

    return {
        "description_markdown": description,
        "pricing": pricing,
        "launch_email": launch_email,
        "social_captions": socials,
        "listing_metadata": listing,
    }


def _description(s, benefits, hooks, pricing):
    b = "\n".join(f"- {x}" for x in benefits)
    hook = hooks[0]
    return f"""# {s.title}
{('*' + s.subtitle + '*') if s.subtitle else ''}

{hook}

**Who this is for:** {s.audience}.

## What you'll get
{b}

## Inside this book
By the end you'll have a repeatable system — not just theory. Each chapter is
short, practical, and ends with a concrete next step so you make progress from
page one.

> "Finally, a guide that gets to the point." — the reader you're writing for

**Instant download.** Read on any device (PDF + EPUB included).
Regular price ${pricing['standard']} — grab it now.

*By {s.author}*
"""


def _launch_email(s, benefits):
    top = benefits[0] if benefits else "get results faster"
    return f"""Subject: It's here — {s.title} 🎉

Hi there,

The wait is over. **{s.title}** is officially live.

If you've ever wanted to {top.lower()}, this is the shortcut. I packed
everything into a focused, no-fluff guide you can finish in a weekend and
start using immediately.

For the next 48 hours it's at the launch price. After that it goes up.

👉 Grab your copy: [LINK]

To your success,
{s.author}
"""


def _socials(s, hooks):
    hook = hooks[0]
    return {
        "twitter_x": f"📘 Just launched: {s.title}\n\n{hook}\n\nGrab it here 👇 [LINK]",
        "instagram": f"NEW: {s.title} is out now! {hook} Link in bio. "
                     f"#ebook #{_slug(s.title)} #selfpublishing",
        "linkedin": f"Excited to share my new eBook — {s.title}.\n\n{hook}\n\n"
                    f"It's a practical, get-it-done guide. Link in comments.",
    }


def _categories(s):
    return ["Nonfiction > Self-Help", "Business & Money > Skills",
            "Education & Reference > How-To"]


def _keywords(s):
    base = _slug(s.title).replace("-", " ")
    return [base, f"{base} guide", f"how to {base}", f"{base} for beginners",
            f"{base} step by step", "ebook", "practical guide"]


def _slug(s: str) -> str:
    return "".join(c if c.isalnum() else "-" for c in s.lower()).strip("-")


def write_sales_kit(kit: dict, out_dir: str) -> str:
    import os
    md_path = os.path.join(out_dir, "sales_kit.md")
    parts = [kit["description_markdown"], "\n---\n## Pricing\n",
             "```json", json.dumps(kit["pricing"], indent=2), "```",
             "\n## Launch email\n", "```", kit["launch_email"], "```",
             "\n## Social captions\n", "```json",
             json.dumps(kit["social_captions"], indent=2), "```",
             "\n## Listing metadata\n", "```json",
             json.dumps(kit["listing_metadata"], indent=2), "```"]
    with open(md_path, "w") as fh:
        fh.write("\n".join(parts))
    with open(os.path.join(out_dir, "sales_kit.json"), "w") as fh:
        json.dump(kit, fh, indent=2)
    return md_path
