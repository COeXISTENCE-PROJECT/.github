#!/usr/bin/env python3

import json
import math
from functools import lru_cache
from io import BytesIO
from pathlib import Path

import requests
from PIL import Image, ImageDraw, ImageFont, ImageFilter


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "static" / "contributors.json"
OUT_DIR = ROOT / "static" / "contributors"
CARDS_DIR = OUT_DIR / "cards"
AVATARS_DIR = OUT_DIR / "avatars"
MEMBER_BG_PATH = OUT_DIR / "coexistence_small.png"

CARD_W = 360
CARD_H = 138
AVATAR_SIZE = 82
AVATAR_RING = 7
RADIUS = 28
SCALE = 3
OUTPUT_DPI = (300, 300)

PANEL_BG = (248, 250, 252)
CARD_BG = (255, 255, 255)
TEXT = (15, 23, 42)
MUTED = (100, 116, 139)
BORDER = (226, 232, 240)

MEMBER_ACCENT = (37, 99, 235)
PROJECT_LEAD_ACCENT = (124, 58, 237)
AFFILIATED_ACCENT = (5, 150, 105)
FORMER_ACCENT = (217, 119, 6)
WATERMARK_TINT = (184, 192, 204)
WATERMARK_ALPHA = 80

FONT_CANDIDATES = [
    "/System/Library/Fonts/Supplemental/Arial Unicode.ttf",
    "/System/Library/Fonts/Supplemental/Arial.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSansCondensed.ttf",
]


def load_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    candidates = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "",
        *FONT_CANDIDATES,
    ]

    for path in candidates:
        if path and Path(path).exists():
            return ImageFont.truetype(path, size)

    return ImageFont.load_default()


def text_size(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.ImageFont):
    box = draw.textbbox((0, 0), text, font=font)
    return box[2] - box[0], box[3] - box[1]


def truncate_text(draw, text, font, max_width):
    if text_size(draw, text, font)[0] <= max_width:
        return text

    ellipsis = "…"
    while text and text_size(draw, text + ellipsis, font)[0] > max_width:
        text = text[:-1]

    return text + ellipsis


def load_fitted_font(
    draw: ImageDraw.ImageDraw,
    text: str,
    max_width: int,
    preferred_size: int,
    min_size: int,
    bold: bool = False,
) -> ImageFont.FreeTypeFont:
    for size in range(preferred_size, min_size - 1, -1):
        font = load_font(size * SCALE, bold=bold)
        if text_size(draw, text, font)[0] <= max_width:
            return font

    return load_font(min_size * SCALE, bold=bold)


def rounded_rect(draw, xy, radius, fill, outline=None, width=1):
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)


def contributor_group(person: dict) -> str:
    group = person.get("group", "").strip().lower()
    if group in {"external", "affiliated"}:
        return "affiliated"
    if group == "former":
        return "former"
    return "member"


def accent_for(person: dict):
    if person.get("role", "").strip().lower() == "project lead":
        return PROJECT_LEAD_ACCENT

    group = contributor_group(person)
    if group == "affiliated":
        return AFFILIATED_ACCENT
    if group == "former":
        return FORMER_ACCENT
    return MEMBER_ACCENT


def save_image(image: Image.Image, path: Path):
    image.save(path, dpi=OUTPUT_DPI)


def is_member_card(person: dict) -> bool:
    return contributor_group(person) == "member"


@lru_cache(maxsize=1)
def load_member_watermark() -> Image.Image | None:
    if not MEMBER_BG_PATH.exists():
        return None

    logo = Image.open(MEMBER_BG_PATH).convert("RGBA")
    alpha = logo.getchannel("A")
    tinted = Image.new("RGBA", logo.size, (*WATERMARK_TINT, 0))
    tinted.putalpha(alpha.point(lambda a: (a * WATERMARK_ALPHA) // 255))
    return tinted


def add_member_watermark(card: Image.Image):
    watermark = load_member_watermark()
    if watermark is None:
        return

    target_h = int(CARD_H * SCALE * 0.9)
    ratio = target_h / watermark.height
    target_w = int(watermark.width * ratio)
    watermark = watermark.resize((target_w, target_h), Image.Resampling.LANCZOS)
    watermark = watermark.filter(ImageFilter.GaussianBlur(1))

    overlay = Image.new("RGBA", card.size, (0, 0, 0, 0))
    wx = int(CARD_W * SCALE * 0.63)
    wy = int((CARD_H * SCALE - target_h) / 2)
    overlay.paste(watermark, (wx, wy), watermark)
    card.alpha_composite(overlay)


def circular_avatar(img: Image.Image, size: int) -> Image.Image:
    img = img.convert("RGB").resize((size, size), Image.Resampling.LANCZOS)

    mask = Image.new("L", (size, size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size, size), fill=255)

    out = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    out.paste(img, (0, 0), mask)
    return out


def download_avatar(github: str) -> Image.Image:
    url = f"https://github.com/{github}.png?size=240"
    cached_avatar = AVATARS_DIR / f"{github.lower()}.png"

    if cached_avatar.exists():
        return Image.open(cached_avatar).convert("RGB")

    try:
        response = requests.get(url, timeout=20)
        response.raise_for_status()
        avatar = Image.open(BytesIO(response.content)).convert("RGB")
        AVATARS_DIR.mkdir(parents=True, exist_ok=True)
        save_image(avatar, cached_avatar)
        return avatar
    except requests.RequestException:
        if cached_avatar.exists():
            return Image.open(cached_avatar).convert("RGB")

        cached_card = CARDS_DIR / f"{github.lower()}.png"
        if cached_card.exists():
            card = Image.open(cached_card).convert("RGB")
            scale = max(1, round(card.width / CARD_W))
            crop_box = (
                28 * scale,
                28 * scale,
                (28 + AVATAR_SIZE) * scale,
                (28 + AVATAR_SIZE) * scale,
            )
            return card.crop(crop_box)
        raise


def make_card(person: dict) -> Image.Image:
    img = Image.new("RGBA", (CARD_W * SCALE, CARD_H * SCALE), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    card_box = (
        8 * SCALE,
        8 * SCALE,
        (CARD_W - 8) * SCALE,
        (CARD_H - 8) * SCALE,
    )

    shadow = Image.new("RGBA", img.size, (0, 0, 0, 0))
    shadow_draw = ImageDraw.Draw(shadow)
    shadow_draw.rounded_rectangle(
        card_box,
        radius=RADIUS * SCALE,
        fill=(15, 23, 42, 28),
    )
    shadow = shadow.filter(ImageFilter.GaussianBlur(10 * SCALE))
    img = Image.alpha_composite(img, shadow)

    card = Image.new("RGBA", img.size, (0, 0, 0, 0))
    card_draw = ImageDraw.Draw(card)
    card_draw.rounded_rectangle(
        card_box,
        radius=RADIUS * SCALE,
        fill=CARD_BG,
        outline=BORDER,
        width=1 * SCALE,
    )

    img = Image.alpha_composite(img, card)
    draw = ImageDraw.Draw(img)

    if is_member_card(person):
        add_member_watermark(img)
        draw = ImageDraw.Draw(img)

    handle_font = load_font(16 * SCALE)
    role_font = load_font(14 * SCALE)

    accent = accent_for(person)

    avatar = download_avatar(person["github"])
    avatar = circular_avatar(avatar, AVATAR_SIZE * SCALE)

    ax = 28 * SCALE
    ay = 28 * SCALE

    # Avatar ring
    draw.ellipse(
        (
            ax - AVATAR_RING * SCALE,
            ay - AVATAR_RING * SCALE,
            ax + AVATAR_SIZE * SCALE + AVATAR_RING * SCALE,
            ay + AVATAR_SIZE * SCALE + AVATAR_RING * SCALE,
        ),
        fill=accent,
    )
    img.paste(avatar, (ax, ay), avatar)

    tx = 132 * SCALE
    max_text_w = (CARD_W - 152) * SCALE

    name_font = load_fitted_font(draw, person["name"], max_text_w, preferred_size=24, min_size=18, bold=True)
    name = person["name"]
    if text_size(draw, name, name_font)[0] > max_text_w:
        name = truncate_text(draw, name, name_font, max_text_w)
    handle = truncate_text(draw, f"@{person['github']}", handle_font, max_text_w)
    role = truncate_text(draw, person["role"], role_font, max_text_w)

    draw.text((tx, 30 * SCALE), name, fill=TEXT, font=name_font)
    draw.text((tx, 62 * SCALE), handle, fill=MUTED, font=handle_font)
    draw.text((tx, 88 * SCALE), role, fill=MUTED, font=role_font)

    return img


def make_panel(data: dict):
    contributors = data["contributors"]

    members = [p for p in contributors if contributor_group(p) == "member"]
    affiliated = [p for p in contributors if contributor_group(p) == "affiliated"]
    former = [p for p in contributors if contributor_group(p) == "former"]
    affiliated_and_former = [*affiliated, *former]
    sections = [
        ("Project members", members),
        ("Affiliated contributors and former members", affiliated_and_former),
    ]
    sections = [(title, people) for title, people in sections if people]

    cols = 5
    gap = 20
    section_gap = 64
    margin = 36

    section_title_h = 42

    panel_w = margin * 2 + cols * CARD_W + (cols - 1) * gap

    def rows_for(people):
        return math.ceil(len(people) / cols)

    def section_height(people):
        rows = rows_for(people)
        return section_title_h + rows * CARD_H + max(0, rows - 1) * gap

    panel_h = margin + sum(section_height(people) for _, people in sections) + margin
    if len(sections) > 1:
        panel_h += section_gap * (len(sections) - 1)

    panel = Image.new("RGBA", (panel_w * SCALE, panel_h * SCALE), (0, 0, 0, 0))
    draw = ImageDraw.Draw(panel)

    section_font = load_font(22 * SCALE, bold=True)

    x = margin * SCALE
    y = margin * SCALE

    def paste_group(title, people, y):
        draw.text((x, y), title, fill=TEXT, font=section_font)
        y += section_title_h * SCALE

        rows = rows_for(people)
        for row in range(rows):
            row_people = people[row * cols : (row + 1) * cols]
            row_width = len(row_people) * CARD_W + max(0, len(row_people) - 1) * gap
            row_x = ((panel_w - row_width) // 2) * SCALE
            cy = y + row * (CARD_H + gap) * SCALE

            for col, person in enumerate(row_people):
                cx = row_x + col * (CARD_W + gap) * SCALE
                card = make_card(person)
                panel.paste(card, (cx, cy), card)

        return y + rows * CARD_H * SCALE + max(0, rows - 1) * gap * SCALE

    for idx, (title, people) in enumerate(sections):
        y = paste_group(title, people, y)
        if idx < len(sections) - 1:
            y += section_gap * SCALE

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    CARDS_DIR.mkdir(parents=True, exist_ok=True)
    AVATARS_DIR.mkdir(parents=True, exist_ok=True)

    save_image(panel, OUT_DIR / "contributors_panel.png")

    for person in contributors:
        card = make_card(person)
        safe_name = person["github"].lower()
        save_image(card, CARDS_DIR / f"{safe_name}.png")


def main():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    make_panel(data)
    print(f"Generated assets in: {OUT_DIR}")


if __name__ == "__main__":
    main()
