import ffmpeg
import sys
import os

def convert_video(input_path, output_dir="converted"):
    os.makedirs(output_dir, exist_ok=True)
    name, _ = os.path.splitext(os.path.basename(input_path))
    mp4_output = os.path.join(output_dir, f"{name}.mp4")
    webm_output = os.path.join(output_dir, f"{name}.webm")

    try:
        # Convert to MP4 (H.264 + AAC)
        print("🎬 Converting to MP4...")
        (
            ffmpeg
            .input(input_path)
            .output(
                mp4_output,
                vcodec='libx264',
                acodec='aac',
                audio_bitrate='192k',
                video_bitrate='2500k',
                preset='medium',
                strict='experimental'
            )
            .run(overwrite_output=True, capture_stdout=True, capture_stderr=True)
        )
        print(f"✅ MP4 created with audio: {mp4_output}")

        # Convert to WebM (VP9 + Vorbis)
        print("🎥 Converting to WebM...")
        (
            ffmpeg
            .input(input_path)
            .output(
                webm_output,
                vcodec='libvpx-vp9',
                acodec='libvorbis',
                audio_bitrate='128k',
                video_bitrate='2000k'
            )
            .run(overwrite_output=True, capture_stdout=True, capture_stderr=True)
        )
        print(f"✅ WebM created with audio: {webm_output}")

    except ffmpeg.Error as e:
        print("❌ FFmpeg error:")
        print(e.stderr.decode())
        raise e

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python video_converter.py <input_video>")
    else:
        convert_video(sys.argv[1])