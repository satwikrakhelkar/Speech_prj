import os
from pydub import AudioSegment
import speech_recognition as sr
from pydub.silence import split_on_silence

recognizer = sr.Recognizer()

def load_chunks(filename):
    # Load audio file and split into chunks based on silence
    print("Loading and splitting audio...")
    long_audio = AudioSegment.from_mp3(filename)
    audio_chunks = split_on_silence(
        long_audio,
        min_silence_len=1800,  # Minimum silence length in ms
        silence_thresh=-17     # Silence threshold in dB
    )
    print(f"Number of chunks found: {len(audio_chunks)}")
    return audio_chunks

def process_audio_chunks(chunks):
    for i, audio_chunk in enumerate(chunks):
        # Create unique filenames for each chunk
        temp_filename = f"temp_chunk_{i}.wav"
        audio_chunk.export(temp_filename, format="wav")
        
        with sr.AudioFile(temp_filename) as source:
            try:
                audio = recognizer.listen(source)
                text = recognizer.recognize_google(audio)
                print(f"Chunk {i + 1}: {text}")
            except sr.UnknownValueError:
                print(f"Chunk {i + 1}: Could not understand the audio.")
            except sr.RequestError as e:
                print(f"Chunk {i + 1}: Request error from Google API - {e}")
            except Exception as ex:
                print(f"Chunk {i + 1}: An unexpected error occurred - {ex}")
        # Remove temporary file after processing
        os.remove(temp_filename)

# Main Execution
filename = './sample_audio/long_audio.mp3'

try:
    chunks = load_chunks(filename)
    process_audio_chunks(chunks)
except FileNotFoundError:
    print("Audio file not found. Please check the path.")
except Exception as e:
    print(f"An error occurred: {e}")

print("Processing complete!")
