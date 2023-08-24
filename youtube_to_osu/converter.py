import os
from youtube_to_osu.youtube_downloader import download
from youtube_to_osu.onset_generation import wav_to_onset
from youtube_to_osu.beatmap_generation import onset_to_beatmap

from settings import (
    INTERNAL_AUDIO_FILENAME,
    INTERNAL_ONSETS_FILENAME,
    BEATMAP_DATA_FILENAME,
)


def convert(youtube_url: str):
    prepare()
    download(youtube_url, INTERNAL_AUDIO_FILENAME)
    wav_to_onset(INTERNAL_AUDIO_FILENAME, INTERNAL_ONSETS_FILENAME)
    onset_to_beatmap(INTERNAL_ONSETS_FILENAME, BEATMAP_DATA_FILENAME)
    cleanup()


def prepare():
    if os.path.exists(BEATMAP_DATA_FILENAME):
        os.remove(BEATMAP_DATA_FILENAME)


def cleanup():
    os.remove("audio.wav")
    os.remove("onsets.txt")
