import os
import pyaudio
import numpy as np
from pydub import AudioSegment
import keyboard

def record_with_manual_stop(filename, sample_rate=44100):
    print("Recording... Press 'q' to stop.")

    audio = pyaudio.PyAudio()

    stream = audio.open(format=pyaudio.paInt16,
                        channels=2,
                        rate=sample_rate,
                        input=True,
                        frames_per_buffer=1024)

    recording = []
    recording_active = True

    while recording_active:
        audio_chunk = np.frombuffer(stream.read(1024), dtype=np.int16)
        recording.append(audio_chunk)

        if keyboard.is_pressed('q'):
            recording_active = False

    stream.stop_stream()
    stream.close()
    audio.terminate()

    audio_data = np.concatenate(recording)

    # Use the directory path you specified previously
    output_directory = r"C:\\Users\\chaitanya\\Desktop\\audio"  # Replace with your actual directory path
    os.makedirs(output_directory, exist_ok=True)
    output_path = os.path.join(output_directory, filename)

    audio_segment = AudioSegment(
        audio_data.tobytes(),
        frame_rate=sample_rate,
        sample_width=audio_data.dtype.itemsize,
        channels=2
    )

    audio_segment.export("C:\\Users\\chaitanya\\Desktop\\audio", format="mp3")

    print(f"Recording saved as {output_path}")

if __name__ == "__main__":
    recording_filename = "recorded_voice.mp3"
    record_with_manual_stop(recording_filename)
