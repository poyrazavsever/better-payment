"""Build the Better Payment logo family from the approved Brandkit export.

The approved symbol paths are copied verbatim (same `d` data) and only placed
with a group transform, so the geometry never changes. The wordmark is Manrope
800 shaped with HarfBuzz and converted to outlines.
"""

import re
import subprocess
from pathlib import Path

import uharfbuzz as hb
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.svgLib.path import parse_path
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont

ROOT = Path(__file__).parent
EXPORT = ROOT / "export"
OUT = ROOT / "family"
RSVG = r"C:\msys64\ucrt64\bin\rsvg-convert.exe"
MAGICK = r"C:\msys64\ucrt64\bin\magick.exe"

INDIGO = "#4338F2"
INK = "#13132B"
WHITE = "#FFFFFF"
BLACK = "#000000"

WORD = "Better Payment"
WEIGHT = 800
TRACKING = -0.02  # em


# ---------- symbol ----------

def symbol_paths():
    svg = (EXPORT / "better-payment-symbol.svg").read_text(encoding="utf-8")
    svg = re.sub(r"<metadata>.*?</metadata>", "", svg, flags=re.S)
    paths = []
    for tag in re.findall(r"<path[^>]*>", svg):
        fill = re.search(r'fill="([^"]+)"', tag).group(1)
        if fill == "none":
            continue
        paths.append(re.search(r' d="([^"]+)"', tag).group(1))
    pen = BoundsPen(None)
    for d in paths:
        parse_path(d, pen)
    return paths, pen.bounds  # (xmin, ymin, xmax, ymax) in SVG coordinates


PATHS, SB = symbol_paths()
SW, SH = SB[2] - SB[0], SB[3] - SB[1]


def symbol_group(x, y, height, color):
    """Place the symbol with its bbox top-left at (x, y) scaled to `height`."""
    s = height / SH
    tx, ty = x - SB[0] * s, y - SB[1] * s
    body = "".join(f'<path d="{d}"/>' for d in PATHS)
    return f'<g fill="{color}" transform="translate({tx:.3f} {ty:.3f}) scale({s:.6f})">{body}</g>'


# ---------- wordmark ----------

def load_font():
    vf = TTFont(ROOT / "fonts" / "Manrope-VF.ttf")
    return instantiateVariableFont(vf, {"wght": WEIGHT})


FONT = load_font()
UPM = FONT["head"].unitsPerEm
CAP = FONT["OS/2"].sCapHeight
GLYPHS = FONT.getGlyphSet()


def shape(text):
    blob = hb.Blob.from_file_path(str(ROOT / "fonts" / "Manrope-VF.ttf"))
    face = hb.Face(blob)
    font = hb.Font(face)
    font.set_variations({"wght": WEIGHT})
    buf = hb.Buffer()
    buf.add_str(text)
    buf.guess_segment_properties()
    hb.shape(font, buf, {"kern": True, "liga": True})
    order = FONT.getGlyphOrder()
    return [(order[i.codepoint], p.x_advance, p.x_offset, p.y_offset) for i, p in zip(buf.glyph_infos, buf.glyph_positions)]


def wordmark_path(text=WORD):
    """Outline path in font units, baseline at y=0, y flipped for SVG. Returns (d, width)."""
    pen = SVGPathPen(GLYPHS)
    x = 0
    track = TRACKING * UPM
    run = shape(text)
    for n, (name, adv, xo, yo) in enumerate(run):
        tp = TransformPen(pen, (1, 0, 0, -1, x + xo, -yo))
        GLYPHS[name].draw(tp)
        x += adv + (track if n < len(run) - 1 else 0)
    return pen.getCommands(), x


WD, WW = wordmark_path()


def wordmark_group(x, baseline, cap_px, color):
    s = cap_px / CAP
    return f'<g fill="{color}" transform="translate({x:.3f} {baseline:.3f}) scale({s:.6f})"><path d="{WD}"/></g>'


# ---------- writers ----------

def svg(w, h, body, bg=None, radius=0, title="Better Payment"):
    rect = f'<rect width="{w}" height="{h}" rx="{radius}" fill="{bg}"/>' if bg else ""
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.0f} {h:.0f}" width="{w:.0f}" height="{h:.0f}" role="img" aria-label="{title}">'
        f"<title>{title}</title>{rect}{body}</svg>\n"
    )


def write(name, content):
    path = OUT / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def png(src, dst, width, height=None):
    dst = OUT / dst
    dst.parent.mkdir(parents=True, exist_ok=True)
    args = [RSVG, "--format", "png", "--width", str(width)]
    if height:
        args += ["--height", str(height)]
    subprocess.run(args + ["--output", str(dst), str(src)], check=True)
    return dst


# ---------- builds ----------

def build_symbol():
    """Square, padded symbol in color / black / white with a 1/8 safe margin."""
    size = 1024
    pad = size / 8
    h = size - 2 * pad
    w = h * SW / SH
    x = (size - w) / 2
    for variant, color in (("color", INDIGO), ("black", BLACK), ("white", WHITE), ("ink", INK)):
        src = write(f"symbol/better-payment-symbol-{variant}.svg", svg(size, size, symbol_group(x, pad, h, color)))
        for px in (16, 20, 24, 32, 48, 64, 128, 256, 512, 1024):
            png(src, f"symbol/png/better-payment-symbol-{variant}-{px}.png", px)


def build_app_icon():
    """White symbol on an indigo rounded square: favicon, app icon, avatar."""
    size = 512
    radius = size * 0.225
    h = size * 0.56
    w = h * SW / SH
    x, y = (size - w) / 2, (size - h) / 2
    body = symbol_group(x, y, h, WHITE)
    src = write("app-icon/better-payment-app-icon.svg", svg(size, size, body, bg=INDIGO, radius=radius))
    square = write("app-icon/better-payment-avatar-square.svg", svg(size, size, body, bg=INDIGO))
    for px in (16, 32, 48, 64, 128, 180, 192, 256, 512, 1024):
        png(src, f"app-icon/png/better-payment-app-icon-{px}.png", px)
    for px in (400, 1024):
        png(square, f"app-icon/png/better-payment-avatar-square-{px}.png", px)
    # favicon set
    write("favicon/favicon.svg", svg(size, size, body, bg=INDIGO, radius=radius))
    for px in (16, 32, 48):
        png(src, f"favicon/favicon-{px}.png", px)
    png(src, "favicon/apple-touch-icon.png", 180)
    png(src, "favicon/icon-192.png", 192)
    png(src, "favicon/icon-512.png", 512)
    subprocess.run(
        [MAGICK, *(str(OUT / f"favicon/favicon-{px}.png") for px in (16, 32, 48)), str(OUT / "favicon/favicon.ico")],
        check=True,
    )


def build_wordmark():
    cap = 100
    s = cap / CAP
    width = WW * s
    asc, desc = 0.78 * cap / 0.72, 0.30 * cap  # generous box around cap height and descender
    h = asc + desc
    for variant, color in (("color", INK), ("black", BLACK), ("white", WHITE)):
        src = write(
            f"wordmark/better-payment-wordmark-{variant}.svg",
            svg(width, h, wordmark_group(0, asc, cap, color)),
        )
        png(src, f"wordmark/png/better-payment-wordmark-{variant}-1200.png", 1200)


def lockup_horizontal(sym_color, text_color, bg=None):
    cap = 100
    sym_h = cap * 1.55
    gap = sym_h * 0.32
    pad = sym_h * 0.25 if bg else 0
    sym_w = sym_h * SW / SH
    text_w = WW * cap / CAP
    w = pad * 2 + sym_w + gap + text_w
    h = pad * 2 + sym_h
    top = pad
    baseline = top + sym_h / 2 + cap / 2  # optical: symbol centred on cap height
    body = symbol_group(pad, top, sym_h, sym_color) + wordmark_group(pad + sym_w + gap, baseline, cap, text_color)
    return svg(w, h, body, bg=bg, radius=h * 0.12 if bg else 0)


def lockup_stacked(sym_color, text_color):
    cap = 100
    sym_h = cap * 2.4
    gap = cap * 0.7
    sym_w = sym_h * SW / SH
    text_w = WW * cap / CAP
    w = max(sym_w, text_w)
    h = sym_h + gap + cap * 1.3  # room for the y descender
    body = symbol_group((w - sym_w) / 2, 0, sym_h, sym_color) + wordmark_group((w - text_w) / 2, sym_h + gap + cap, cap, text_color)
    return svg(w, h, body)


def build_lockups():
    for variant, (sc, tc) in {
        "color": (INDIGO, INK),
        "black": (BLACK, BLACK),
        "white": (WHITE, WHITE),
    }.items():
        h = write(f"lockup/better-payment-horizontal-{variant}.svg", lockup_horizontal(sc, tc))
        png(h, f"lockup/png/better-payment-horizontal-{variant}-1600.png", 1600)
        st = write(f"lockup/better-payment-stacked-{variant}.svg", lockup_stacked(sc, tc))
        png(st, f"lockup/png/better-payment-stacked-{variant}-1000.png", 1000)
    banner = write("lockup/better-payment-horizontal-on-indigo.svg", lockup_horizontal(WHITE, WHITE, bg=INDIGO))
    png(banner, "lockup/png/better-payment-horizontal-on-indigo-1600.png", 1600)


if __name__ == "__main__":
    build_symbol()
    build_app_icon()
    build_wordmark()
    build_lockups()
    print("symbol bbox", [round(v, 1) for v in SB], "aspect", round(SW / SH, 3))
    print("wordmark width/cap", round(WW / CAP, 3))
