"""Turn raw Kling icon loops into web-ready, white-levelled, tightly cropped loops."""

import json
import re
import subprocess
from pathlib import Path

HERE = Path(__file__).parent
MAGICK = r"C:\msys64\ucrt64\bin\magick.exe"
NAMES = "unified-api callback threeds refund cancel installments status events plugin edge sandbox languages handler idempotency docs".split()
OUT = HERE / "web"
OUT.mkdir(exist_ok=True)


def run(*args):
    return subprocess.run(args, check=True, capture_output=True, text=True)


def probe(src):
    out = run("ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height,nb_frames", "-of", "json", str(src)).stdout
    s = json.loads(out)["streams"][0]
    return int(s["width"]), int(s["height"]), int(s.get("nb_frames") or 120)


def frame(src, n, dst):
    run("ffmpeg", "-v", "error", "-y", "-i", str(src), "-vf", f"select=eq(n\\,{n})", "-frames:v", "1", str(dst))


def bg_color(png):
    out = run(MAGICK, str(png), "-format", "%[pixel:p{4,4}]", "info:").stdout
    r, g, b = (int(v) for v in re.findall(r"\d+", out)[:3])
    return r, g, b


def bbox(png, bg):
    # pixels that differ from the background by more than a few levels
    hexbg = "#%02x%02x%02x" % bg
    out = run(MAGICK, str(png), "-fuzz", "2%", "-fill", "white", "-opaque", hexbg, "-fuzz", "0", "-trim", "-format", "%@", "info:").stdout
    m = re.match(r"(\d+)x(\d+)\+(\d+)\+(\d+)", out.strip())
    w, h, x, y = (int(v) for v in m.groups())
    return x, y, x + w, y + h


def rmse(a, b):
    out = subprocess.run([MAGICK, "compare", "-metric", "RMSE", str(a), str(b), "null:"], capture_output=True, text=True).stderr
    return float(re.search(r"\(([\d.e-]+)\)", out).group(1))


report = {}
for name in NAMES:
    src = HERE / f"{name}.mp4"
    W, H, N = probe(src)
    tmp = HERE / "_f"
    tmp.mkdir(exist_ok=True)
    samples = [0, N // 6, N // 3, N // 2, 2 * N // 3, 5 * N // 6, N - 1]
    boxes, bg = [], None
    for i, n in enumerate(samples):
        p = tmp / f"{name}-{i}.png"
        frame(src, n, p)
        if bg is None:
            bg = bg_color(p)
        boxes.append(bbox(p, bg))
    x0 = min(b[0] for b in boxes); y0 = min(b[1] for b in boxes)
    x1 = max(b[2] for b in boxes); y1 = max(b[3] for b in boxes)
    side = int(max(x1 - x0, y1 - y0) * 1.22)
    side = min(side, W, H)
    cx, cy = (x0 + x1) // 2, (y0 + y1) // 2
    cx0 = max(0, min(W - side, cx - side // 2)); cy0 = max(0, min(H - side, cy - side // 2))
    levels = "colorlevels=rimax=%.4f:gimax=%.4f:bimax=%.4f" % tuple(c / 255 * 0.985 for c in bg)
    vf = f"{levels},crop={side}:{side}:{cx0}:{cy0},scale=480:480:flags=lanczos"
    base = OUT / f"icon-{name}"
    run("ffmpeg", "-v", "error", "-y", "-i", str(src), "-vf", vf, "-an", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "22", "-preset", "slow", "-movflags", "+faststart", f"{base}.mp4")
    run("ffmpeg", "-v", "error", "-y", "-i", str(src), "-vf", vf, "-an", "-c:v", "libvpx-vp9", "-b:v", "0", "-crf", "34", "-row-mt", "1", f"{base}.webm")
    run("ffmpeg", "-v", "error", "-y", "-i", f"{base}.mp4", "-frames:v", "1", f"{base}-poster.png")
    seam = rmse(tmp / f"{name}-0.png", tmp / f"{name}-{len(samples) - 1}.png")
    corner = run(MAGICK, f"{base}-poster.png", "-format", "%[pixel:p{2,2}]", "info:").stdout
    report[name] = {"bg": bg, "crop": side, "seam_rmse": round(seam, 4), "corner": corner, "kb": Path(f"{base}.mp4").stat().st_size // 1024}
    print(name, report[name], flush=True)

(OUT / "report.json").write_text(json.dumps(report, indent=2))
