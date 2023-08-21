from pytube import YouTube

video_url = 'https://www.youtube.com/watch?v=feq6MOg3qpA'

# Create a YouTube object
yt = YouTube(video_url)

# Choose the highest quality stream
stream = yt.streams.get_audio_only()

# Set the output file name
output_file = 'output.mp4'

# Download the stream
stream.download(output_path='', filename=output_file)

print(f"Video '{yt.title}' downloaded as {output_file}")
