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
    format(download_path, output_file_name, "pcm_s16le")  # For internal use
    format(download_path, "beatmap.mp3", "mp3")  # For use in Osu

    # Cleanup
    os.remove(download_path)


def format(input_file_name, output_file_name, codec):
    (
        ffmpeg.input(input_file_name)
        .output(output_file_name, codec=codec, ac=2, ar="44100")
        .run(capture_stdout=True, capture_stderr=True)
    )
