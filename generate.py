import sys
import numpy as np
import aubio
import wave

# Onset detection parameters
WIN_S = 512                 # fft size
HOP_S = WIN_S // 2          # hop size

# Beep parameters
BEEP_FREQ = 4000  # Beep frequency in Hz
BEEP_DURATION = 0.001  # Beep duration in seconds

def wavToOnset(audio_input_filename, audio_output_filename, onset_output_filename, sample_rate = 0):
    s = aubio.source(audio_input_filename, sample_rate, HOP_S)
    sample_rate = s.samplerate
    
    o = aubio.onset("default", WIN_S, HOP_S, sample_rate)
    
    # List of onsets, in samples
    onsets = []

    # Open the onset output file for writing
    onset_output_file = open(onset_output_filename, 'w')

    # Total number of frames read
    total_frames = 0
    while True:
        samples, read = s()
        if o(samples):
            onset_sample = o.get_last()
            onset_ms = round(onset_sample / float(sample_rate) * 1000.0)  # Round onset sample to the nearest whole number in milliseconds
            print("Onset detected at sample:", onset_sample, " (", onset_ms, " ms)")
            onsets.append(onset_sample)
            onset_output_file.write(str(onset_ms) + '\n')  # Write onset time to the file
        total_frames += read
        if read < HOP_S:
            break

    # Close the onset output file
    onset_output_file.close()

    # Calculate the number of notes and average NPS
    number_of_notes = len(onsets)
    song_length_seconds = total_frames / sample_rate
    average_nps = number_of_notes / song_length_seconds

    print("Number of notes:", number_of_notes)
    print("Song length (seconds):", song_length_seconds)
    print("Average NPS:", average_nps)

    # Generate rhythm audio with short beep at note onsets
    beep_samples = int(BEEP_DURATION * sample_rate)
    rhythm_audio = np.zeros(total_frames)

    for onset_sample in onsets:
        start = onset_sample - beep_samples // 2
        end = start + beep_samples
        if start >= 0 and end < len(rhythm_audio):
            beep = np.sin(2 * np.pi * BEEP_FREQ * np.arange(beep_samples) / float(sample_rate))
            rhythm_audio[start:end] += beep

    # Normalize the audio
    rhythm_audio /= np.max(np.abs(rhythm_audio))

    # Save the generated rhythm audio to a WAV file
    output_wave = wave.open(audio_output_filename, 'wb')
    output_wave.setnchannels(1)
    output_wave.setsampwidth(2)
    output_wave.setframerate(sample_rate)
    output_wave.writeframes((rhythm_audio * 32767).astype(np.int16).tobytes())
    output_wave.close()

    print("Rhythm file saved as", audio_output_filename)