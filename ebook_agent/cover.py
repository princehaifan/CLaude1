"""Cover generation for eBooks.

Produces a clean, professional cover image (default 1600x2560, the KDP-friendly
1.6 ratio) using Pillow only — no external services required. Colors are derived
deterministically from the title so every book gets its own look, or you can pass
an explicit palette.
"""

from __future__ import annotations

import hashlib
import textwrap
from dataclasses import dataclass, field

from PIL import Image, ImageDraw, ImageFont

# A curated set of tasteful gradient palettes (top, bottom, accent, text).
_PALETTES = [
    ((14, 22, 48), (34, 58, 122), (255, 209, 102), (245, 247, 255)),
    ((28, 12, 40), (92, 32, 96), (255, 138, 138), (250, 245, 255)),
    ((10, 38, 34), (18, 96, 82), (247, 200, 115), (240, 255, 250)),
    ((40, 16, 16), (120, 42, 34), (255, 214, 140), (255, 245, 240)),
    ((12, 20, 28), (24, 52, 74), (120, 220, 232), (238, 248, 252)),
    ((26, 22, 12), (78, 62, 24), (240, 214, 120), (252, 249, 238)),
]


@dataclass
class CoverSpec:
    title: str
    author: str = ""
    subtitle: str = ""
    width: int = 1600
    height: int = 2560
    palette: tuple | None = None  # (top, bottom, accent, text)
    badge: str = ""  # optional small top ribbon text, e.g. "2025 EDITION"
    fonts: dict = field(default_factory=dict)


def _pick_palette(seed: str) -> tuple:
    idx = int(hashlib.sha256(seed.encode()).hexdigest(), 16) % len(_PALETTES)
    return _PALETTES[idx]


def _load_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    candidates = (
        [
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
            "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
        ]
        if bold
        else [
            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
            "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
        ]
    )
    for path in candidates:
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue
    return ImageFont.load_default()


def _vertical_gradient(w: int, h: int, top: tuple, bottom: tuple) -> Image.Image:
    base = Image.new("RGB", (w, h), top)
    draw = ImageDraw.Draw(base)
    for y in range(h):
        t = y / max(h - 1, 1)
        r = int(top[0] + (bottom[0] - top[0]) * t)
        g = int(top[1] + (bottom[1] - top[1]) * t)
        b = int(top[2] + (bottom[2] - top[2]) * t)
        draw.line([(0, y), (w, y)], fill=(r, g, b))
    return base


def _fit_font(draw, text, max_width, start_size, bold=True, min_size=28):
    """Return the largest font size whose wrapped lines fit max_width."""
    size = start_size
    while size > min_size:
        font = _load_font(size, bold=bold)
        avg = max(draw.textlength("n", font=font), 1)
        chars = max(int(max_width / avg), 6)
        lines = []
        for para in text.split("\n"):
            lines.extend(textwrap.wrap(para, width=chars) or [""])
        if all(draw.textlength(ln, font=font) <= max_width for ln in lines):
            return font, lines
        size -= 4
    font = _load_font(min_size, bold=bold)
    avg = max(draw.textlength("n", font=font), 1)
    chars = max(int(max_width / avg), 6)
    lines = []
    for para in text.split("\n"):
        lines.extend(textwrap.wrap(para, width=chars) or [""])
    return font, lines


def generate_cover(spec: CoverSpec, out_path: str) -> str:
    w, h = spec.width, spec.height
    top, bottom, accent, text_color = spec.palette or _pick_palette(spec.title)

    img = _vertical_gradient(w, h, top, bottom)
    draw = ImageDraw.Draw(img, "RGBA")

    margin = int(w * 0.09)
    inner_w = w - 2 * margin

    # Subtle decorative accent bars near the top.
    draw.rectangle([margin, int(h * 0.11), margin + int(inner_w * 0.28), int(h * 0.115)],
                   fill=accent)

    # Optional badge ribbon.
    if spec.badge:
        bfont = _load_font(int(w * 0.028), bold=True)
        btext = spec.badge.upper()
        tw = draw.textlength(btext, font=bfont)
        pad = int(w * 0.02)
        by = int(h * 0.05)
        draw.rounded_rectangle(
            [margin, by, margin + tw + 2 * pad, by + int(w * 0.055)],
            radius=int(w * 0.012), fill=accent)
        draw.text((margin + pad, by + int(w * 0.012)), btext, font=bfont, fill=top)

    # Title — big, bold, top third.
    title_font, title_lines = _fit_font(
        draw, spec.title.upper(), inner_w, int(w * 0.14), bold=True)
    y = int(h * 0.16)
    for line in title_lines:
        draw.text((margin, y), line, font=title_font, fill=text_color)
        y += int(title_font.size * 1.12)

    # Subtitle.
    if spec.subtitle:
        y += int(h * 0.012)
        sub_font, sub_lines = _fit_font(
            draw, spec.subtitle, inner_w, int(w * 0.055), bold=False, min_size=22)
        for line in sub_lines:
            draw.text((margin, y), line, font=sub_font, fill=accent)
            y += int(sub_font.size * 1.25)

    # Author — bottom.
    if spec.author:
        af = _load_font(int(w * 0.05), bold=True)
        atext = spec.author.upper()
        aw = draw.textlength(atext, font=af)
        ay = int(h * 0.9)
        draw.line([(margin, ay - int(h * 0.02)), (margin + int(inner_w * 0.35), ay - int(h * 0.02))],
                  fill=accent, width=4)
        draw.text((margin, ay), atext, font=af, fill=text_color)
        _ = aw

    img.save(out_path, quality=95)
    return out_path
