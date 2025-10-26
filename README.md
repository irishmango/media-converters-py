# Python Mini Projects: Media Converters

Utilities to convert videos (to MP4 and WebM) and batch-convert images to WebP.

## Requirements

- macOS (tested), Linux/Windows should also work
- Python 3.8+
- FFmpeg command-line tools installed (required for video conversion)
- Python packages from `requirements.txt`

### Install FFmpeg (macOS)

```bash
# Using Homebrew
brew update
brew install ffmpeg
```

Verify:

```bash
ffmpeg -version
```

## Setup

```bash
# From the project root
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

### 1 Video converter

Script: `video_converter.py`

Converts a single input video into:
- MP4 (H.264 video + AAC audio)
- WebM (VP9 video + Vorbis audio)

Outputs are saved under `converted/`.

Run:

```bash
python video_converter.py path/to/input_video.mov
```

Example:

```bash
python video_converter.py assets/convert/sample.mov
```

Notes:
- The script auto-creates `converted/`.
- Filenames are based on the input name, e.g. `sample.mp4` and `sample.webm`.
- If you see an error about FFmpeg missing, install it with Homebrew (see above).

### 2 Image converter → WebP

Script: `image_converter.py`

Batch-converts images in a folder to WebP. Supported inputs: `.jpg`, `.jpeg`, `.png`, `.bmp`, `.tiff`.

By default, it reads from `assets/convert` and writes to `converted_webp/` with quality 80.

Run with explicit arguments:

```bash
# Usage: python image_converter.py <input_dir> [output_dir] [quality]
python image_converter.py assets/convert converted_webp 80
```

Or with no arguments (uses defaults):

```bash
python image_converter.py
```

Outputs are written to `converted_webp/`.

## Project structure

```
image_converter.py       # Batch image → WebP converter
video_converter.py       # Single video → MP4 + WebM converter
assets/convert/          # Place sample inputs here (optional)
converted/               # MP4/WebM outputs (created automatically)
converted_webp/          # WebP outputs (created automatically)
requirements.txt         # Python dependencies
```

## Troubleshooting

- ffmpeg: command not found
  - Install via Homebrew: `brew install ffmpeg`
  - Ensure it’s on your PATH: `which ffmpeg`

- PIL/Pillow or ffmpeg-python not found
  - Install deps: `pip install -r requirements.txt`

## License

MIT (or your preferred license).
