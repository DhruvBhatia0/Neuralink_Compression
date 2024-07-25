# this is a file aimed at extracting metadata about the wav files

import wave

def get_wav_metadata(filename):
   with wave.open(filename, 'rb') as wav_file:
       channels = wav_file.getnchannels()
       sample_width = wav_file.getsampwidth()
       framerate = wav_file.getframerate()
       n_frames = wav_file.getnframes()
       
       print(f"Number of channels: {channels}")
       print(f"Sample width: {sample_width} bytes")
       print(f"Frame rate: {framerate} Hz")
       print(f"Number of frames: {n_frames}")
       print(f"Duration: {n_frames / float(framerate):.2f} seconds")

# Usage
get_wav_metadata('data/0aefe960-43fd-41cc-97c8-bf9d2d64efd3.wav')
