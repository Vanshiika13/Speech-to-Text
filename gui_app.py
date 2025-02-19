from deep_translator import GoogleTranslator # type: ignore
import speech_recognition as sr # type: ignore
import tkinter as tk
from tkinter import messagebox

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        messagebox.showinfo("Info", "🎤 Speak Now...")
        try:
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio)
            
            output_label.config(text="Recognized: " + text)
            
            # Translate the recognized text
            translated_text = translate_text(text, selected_language.get())
            translated_label.config(text="Translated: " + translated_text)
            
            # Save both original and translated text to a file
            with open("translated_text.txt", "w", encoding="utf-8") as file:
                file.write(f"Original: {text}\nTranslated: {translated_text}")  # ✅ Correct indentation
            
            messagebox.showinfo("Success", "✅ Speech recognized and translated successfully!")

        except sr.UnknownValueError:
            messagebox.showerror("Error", "❌ Could not understand the speech")
        except sr.RequestError:
            messagebox.showerror("Error", "❌ Could not connect to Google Speech API")


def translate_text(text, target_lang):
    translator = GoogleTranslator(source='auto', target=target_lang) # type: ignore
    return translator.translate(text)


# GUI Setup
root = tk.Tk()
root.title("Speech to Text & Translation")
root.geometry("500x400")

record_button = tk.Button(root, text="🎤 Start Recording", command=recognize_speech, font=("Arial", 14))
record_button.pack(pady=10)

output_label = tk.Label(root, text="Speech Output Will Appear Here", wraplength=450, font=("Arial", 12))
output_label.pack(pady=10)

# Language selection dropdown
languages = {"English": "en", "Hindi": "hi", "French": "fr", "Spanish": "es", "German": "de"}
selected_language = tk.StringVar(root)
selected_language.set("hi")  # Default language is Hindi

language_menu = tk.OptionMenu(root, selected_language, *languages.values())
language_menu.pack(pady=5)

translated_label = tk.Label(root, text="Translated Text Will Appear Here", wraplength=450, font=("Arial", 12))
translated_label.pack(pady=10)

root.mainloop()
