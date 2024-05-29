import argparse
from moviepy.editor import AudioFileClip, ImageClip, concatenate_videoclips

def convert_m4b_to_mp4(audio_path, image_path, output_path, duration=None, fps=24):
    # Load the audio file
    audio = AudioFileClip(audio_path)
    
    if duration:
        audio = audio.subclip(0, duration)

    # Load the image file
    image = ImageClip(image_path).set_duration(audio.duration).set_fps(fps)
    
    # Set the audio to the image clip
    video = image.set_audio(audio)
    
    # Write the result to a file
    video.write_videofile(output_path, codec='libx264', audio_codec='aac')

def main():
    parser = argparse.ArgumentParser(description="Convert .m4b audio file to .mp4 video file with a static image.")
    parser.add_argument('audio', type=str, help="Path to the input .m4b audio file")
    parser.add_argument('image', type=str, help="Path to the static image file to be used for the video")
    parser.add_argument('output', type=str, help="Path to the output .mp4 video file")
    parser.add_argument('--duration', type=int, help="Duration of the video in seconds", default=None)
    parser.add_argument('--fps', type=int, help="Frame rate of the output video", default=24)

    args = parser.parse_args()
    
    convert_m4b_to_mp4(args.audio, args.image, args.output, args.duration, args.fps)

if __name__ == "__main__":
    main()
