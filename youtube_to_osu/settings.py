WAV_CODEC = "pcm_s16le"
MP3_CODEC = "mp3"

BEATMAP_AUDIO_FILENAME = "beatmap.mp3"
BEATMAP_DATA_FILENAME = "beatmap.txt"
INTERNAL_AUDIO_FILENAME = "audio.wav"
INTERNAL_ONSETS_FILENAME = "onsets.txt"

POSSIBLE_LANE_NUMBERS = [64, 192, 320, 448]

# Onset detection parameters
WIN_S = 512  # fft size
HOP_S = WIN_S // 2  # hop size

# Beep parameters
BEEP_FREQ = 4000  # Beep frequency in Hz
BEEP_DURATION = 0.001  # Beep duration in seconds

DEFAULT_SAMPLERATE = 0
