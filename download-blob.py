import subprocess

# Replace this with the .m3u8 or .mpd link found in your browser network tab
manifest_url = "https://cdn.abc.com/hls/480p,720p,1080p,.mp4.urlset/master.m3u8?hash=xyz"
output_file = "downloaded_video.mp4"

# Use FFmpeg to automatically stream, stitch, and convert the video chunks
command = [
    'ffmpeg',
    '-i', manifest_url,   # Input URL
    '-c', 'copy',          # Copy the streams without re-encoding (keeps quality, very fast)
    '-bsf:a', 'aac_adtstoasc', # Fix potential audio container sync issues
    output_file            # Output destination
]

try:
    print("Downloading and converting video stream...")
    subprocess.run(command, check=True)
    print(f"Success! Saved as {output_file}")
except subprocess.CalledProcessError as e:
    print(f"An error occurred: {e}")