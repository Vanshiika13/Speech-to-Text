import speech_recognition as sr   # type: ignore

def speech_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("🎤 Speak something...")
        recognizer.adjust_for_ambient_noise(source)  # Reduce background noise
        audio = recognizer.listen(source)  # Capture speech

    try:
        text = recognizer.recognize_google(audio)  # Convert speech to text
        print(f"📝 Recognized Text: {text}")

        # Save text to a file
        with open("output.txt", "w", encoding="utf-8") as file:
            file.write(text)
        print("✅ Text saved to output.txt")

    except sr.UnknownValueError:
        print("❌ Sorry, could not understand the audio.")
    except sr.RequestError:
        print("❌ Could not request results from Google Speech API.")

if __name__ == "__main__":
    speech_to_text()
