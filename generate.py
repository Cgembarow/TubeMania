import sys
import numpy as np
import aubio
import wave

# Onset detection parameters
win_s = 512                 # fft size
hop_s = win_s // 2          # hop size

# Beep parameters
beep_freq = 4000  # Beep frequency in Hz
beep_duration = 0.001  # Beep duration in seconds

# Input and output filenames
input_filename = sys.argv[1]
output_filename = 'temp_output/vocals_rythm.wav'
onset_output_filename = 'temp_output/output_onset.txt'  # New output file for onset times

if len(sys.argv) < 2:
    print("Usage: %s <filename>" % sys.argv[0])
    sys.exit(1)

samplerate = 0
if len(sys.argv) > 2:
    samplerate = int(sys.argv[2])

s = aubio.source(input_filename, samplerate, hop_s)
samplerate = s.samplerate

o = aubio.onset("default", win_s, hop_s, samplerate)

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
        onset_ms = round(onset_sample / float(samplerate) * 1000.0)  # Round onset sample to the nearest whole number in milliseconds
        print("Onset detected at sample:", onset_sample, " (", onset_ms, " ms)")
        onsets.append(onset_sample)
        onset_output_file.write(str(onset_ms) + '\n')  # Write onset time to the file
    total_frames += read
    if read < hop_s:
        break

# Close the onset output file
onset_output_file.close()

# Rest of your code remains the same...

# Calculate the number of notes and average NPS
number_of_notes = len(onsets)
song_length_seconds = total_frames / samplerate
average_nps = number_of_notes / song_length_seconds

print("Number of notes:", number_of_notes)
print("Song length (seconds):", song_length_seconds)
print("Average NPS:", average_nps)

# Generate rhythm audio with short beep at note onsets
beep_samples = int(beep_duration * samplerate)
rhythm_audio = np.zeros(total_frames)

for onset_sample in onsets:
    start = onset_sample - beep_samples // 2
    end = start + beep_samples
    if start >= 0 and end < len(rhythm_audio):
        beep = np.sin(2 * np.pi * beep_freq * np.arange(beep_samples) / float(samplerate))
        rhythm_audio[start:end] += beep

# Normalize the audio
rhythm_audio /= np.max(np.abs(rhythm_audio))

# Save the generated rhythm audio to a WAV file
output_wave = wave.open(output_filename, 'wb')
output_wave.setnchannels(1)
output_wave.setsampwidth(2)
output_wave.setframerate(samplerate)
output_wave.writeframes((rhythm_audio * 32767).astype(np.int16).tobytes())
output_wave.close()

print("Rhythm file saved as", output_filename)
