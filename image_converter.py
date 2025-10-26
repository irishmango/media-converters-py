import os
from PIL import Image

def convert_images_to_webp(input_dir, output_dir="converted_webp", quality=80):
    os.makedirs(output_dir, exist_ok=True)

    supported_formats = (".jpg", ".jpeg", ".png", ".bmp", ".tiff")
    converted_count = 0

    for filename in os.listdir(input_dir):
        if filename.lower().endswith(supported_formats):
            input_path = os.path.join(input_dir, filename)
            name, _ = os.path.splitext(filename)
            output_path = os.path.join(output_dir, f"{name}.webp")

            try:
                with Image.open(input_path) as img:
                    img.save(output_path, "webp", quality=quality)
                converted_count += 1
                print(f"✅ Converted: {filename} → {output_path}")
            except Exception as e:
                print(f"❌ Error converting {filename}: {e}")

    print(f"\n🎉 Done! {converted_count} images converted to WebP.")

if __name__ == "__main__":
    import sys

    if len(sys.argv) >= 2:
        input_dir = sys.argv[1]
        output_dir = sys.argv[2] if len(sys.argv) > 2 else "converted_webp"
        quality = int(sys.argv[3]) if len(sys.argv) > 3 else 80
        convert_images_to_webp(input_dir, output_dir, quality)
    else:
        # Default fallback (no arguments required)
        convert_images_to_webp("assets/convert")