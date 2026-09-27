#!/usr/bin/env python3
import json
import subprocess
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
mode = sys.argv[1] if len(sys.argv) > 1 else "preview"
if mode not in {"preview", "master"}:
    raise SystemExit("usage: render.py preview|master")

w, h = (540, 960) if mode == "preview" else (1080, 1920)
font_size = 34 if mode == "preview" else 68
small_size = 29 if mode == "preview" else 58
margin = 50 if mode == "preview" else 100
font = "/usr/share/fonts/dejavu-sans-fonts/DejaVuSans-Bold.ttf"
source = root / "assets/pexels-33194181.mp4"
audio = root / "assets/narracao-preview.mp3"
out = root / "output" / f"L08-C01-{mode}.mp4"

# Five footage segments use different temporal windows; the fourth is mirrored
# to avoid implying several distinct approved sources. Final two seconds are native typography.
segments = [
    ("0", "3", ""),
    ("3", "8", ""),
    ("6", "12", ""),
    ("0", "6", ",hflip"),
    ("7.2", "12.2", ""),
]
parts = [f"[0:v]split={len(segments)}" + "".join(f"[s{i}]" for i in range(len(segments))) + ";"]
for i, (start, end, extra) in enumerate(segments):
    parts.append(
        f"[s{i}]trim=start={start}:end={end},setpts=PTS-STARTPTS,"
        f"scale={w}:{h}:force_original_aspect_ratio=increase,crop={w}:{h}{extra},"
        f"fps=25,format=yuv420p[v{i}];"
    )
parts.append(f"color=c=0x111111:s={w}x{h}:r=25:d=2,format=yuv420p[v5];")
parts.append("".join(f"[v{i}]" for i in range(6)) + "concat=n=6:v=1:a=0[base];")
parts.append("[base]drawbox=x=0:y=0:w=iw:h=ih:color=black@0.34:t=fill:enable='lt(t,25)',drawbox=x=0:y=0:w=iw:h=ih:color=0x111111@1:t=fill:enable='gte(t,25)'[dim];")

beats = [
    ("beat-01.txt", 0, 3, font_size),
    ("beat-02.txt", 3, 8, font_size),
    ("beat-03.txt", 8, 14, small_size),
    ("beat-04.txt", 14, 20, small_size),
    ("beat-05.txt", 20, 25, small_size),
    ("beat-06.txt", 25, 27, font_size),
]
last = "dim"
for idx, (filename, start, end, size) in enumerate(beats):
    nxt = f"t{idx}"
    textfile = (root / "edit" / filename).as_posix().replace(":", "\\:")
    parts.append(
        f"[{last}]drawbox=x={margin}:y={int(h*0.21)}:w={12 if mode == 'preview' else 24}:h={int(h*0.58)}:color=0xF36C21@1:t=fill:enable='between(t,{start},{end})',"
        f"drawtext=fontfile={font}:textfile='{textfile}':fontcolor=white:fontsize={size}:"
        f"line_spacing={int(size*0.35)}:x=(w-text_w)/2:y=(h-text_h)/2:"
        f"box=1:boxcolor=black@0.22:boxborderw={int(size*0.38)}:enable='between(t,{start},{end})'[{nxt}];"
    )
    last = nxt
parts.append(f"[{last}]format=yuv420p[vout];")
parts.append("[1:a]atempo=1.18,aresample=48000,apad=pad_dur=27,atrim=duration=27[aout]")
filter_complex = "".join(parts)

cmd = [
    "ffmpeg", "-y", "-v", "warning",
    "-i", str(source), "-i", str(audio),
    "-filter_complex", filter_complex,
    "-map", "[vout]", "-map", "[aout]",
    "-t", "27", "-r", "25", "-c:v", "libx264",
    "-preset", "veryfast",
    "-crf", "28" if mode == "preview" else "20",
    "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "128k",
    "-movflags", "+faststart", str(out)
]
subprocess.run(cmd, check=True)
probe = subprocess.run([
    "ffprobe", "-v", "error", "-print_format", "json",
    "-show_format", "-show_streams", str(out)
], check=True, capture_output=True, text=True)
(root / "output" / f"L08-C01-{mode}-probe.json").write_text(probe.stdout, encoding="utf-8")
(root / "edit" / f"command-{mode}.json").write_text(json.dumps(cmd, ensure_ascii=False, indent=2), encoding="utf-8")
print(out)
