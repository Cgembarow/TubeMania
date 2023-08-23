import os
import re

import ffmpeg
from pytube import YouTube


def download(video_url: str, output_file_name: str):
    # If the last 3 characters arent .wav, add .wav to the end of output_file_name
    if output_file_name[-4:] != ".wav":
        output_file_name += ".wav"

    # Create a YouTube object
    yt = YouTube(video_url)

    # Get the audio-only stream and download it
    audio_stream = yt.streams.filter(only_audio=True).first()
    download_path = audio_stream.download()

    # Convert the downloaded audio file to wav with ffmpeg
    input_stream = ffmpeg.input(download_path)
    output_stream = ffmpeg.output(
        input_stream, output_file_name, acodec="pcm_s16le", ac=2, ar="44100"
    )

    # Convert
    ffmpeg.run(output_stream, capture_stdout=True, capture_stderr=True)

    # Cleanup
    os.remove(download_path)
