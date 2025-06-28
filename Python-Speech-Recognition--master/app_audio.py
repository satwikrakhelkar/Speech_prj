import speech_recognition as sr

recognizer = sr.Recognizer()

try:
    # Recording the sound
    with sr.AudioFile("./sample_audio/speech.wav") as source:
        print("Processing the audio file...")
        recorded_audio = recognizer.listen(source)
        print("Audio recording complete.")

    # Recognizing the Audio
    print("Recognizing the text...")
    text = recognizer.recognize_google(recorded_audio, language="en-US")
    print(f"Decoded Text: {text}")

except FileNotFoundError:
    print("The specified audio file was not found.")
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand the audio.")
except sr.RequestError as e:
    print(f"Could not request results from Google Speech Recognition service; {e}")
except Exception as ex:
    print(f"An unexpected error occurred: {ex}")
