import os
from youtube_to_osu.youtube_downloader import download
from youtube_to_osu.onset_generation import wav_to_onset
from youtube_to_osu.beatmap_generation import onset_to_beatmap


def convert(youtube_url: str):
    download(youtube_url, "audio.wav")
    wav_to_onset("audio.wav", "onsets.txt")
    onset_to_beatmap("onsets.txt", "beatmap.txt")
    cleanup()


def cleanup():
    os.remove("audio.wav")
    os.remove("onsets.txt")
