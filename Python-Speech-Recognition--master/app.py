import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# List available microphones
print("Available microphones:")
microphones = sr.Microphone.list_microphone_names()
for index, name in enumerate(microphones):
    print(f"{index}: {name}")

# Use the default microphone
try:
    with sr.Microphone() as source:
        print("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        print("Recording for 4 seconds...")
        recorded_audio = recognizer.listen(source, timeout=4)
        print("Recording complete.")

    # Recognize the recorded audio
    try:
        print("Recognizing the text...")
        text = recognizer.recognize_google(recorded_audio, language="en-US")
        print(f"Decoded Text: {text}")

    except sr.UnknownValueError:
        print("Could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

except Exception as ex:
    print(f"Error: {ex}")

