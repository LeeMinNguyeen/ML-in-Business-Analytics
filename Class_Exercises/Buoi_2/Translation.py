import os
import tkinter as tk
from tkinter import ttk
import requests

class TextTranslatorApp:
    def __init__ (self, root):
        self.root = root
        root.title("Text Translator")

        self.create_widgets()

    def create_widgets(self):
        original_text = tk.Label(self.root, text="Enter text to translate:")
        self.entry = tk.Entry(self.root, width=50)

        orginal_lang = tk.Label(self.root, text="Choose source language:")
        self.source_lang = ttk.Combobox(self.root, values=["en", "es", "fr", "vi", "ja", "zh"])
        self.source_lang.set("en")

        target_lang = tk.Label(self.root, text="Choose target language:")
        self.target_lang = ttk.Combobox(self.root, values=["en", "es", "fr", "vi", "ja", "zh"])
        self.target_lang.set("vi")

        translate_button = tk.Button(self.root, text="Translate", command=self.translate_text) # Button to translate text -> activate translate_text function

        self.result_label = tk.Label(self.root, text="Translated text will appear here.")
        
        original_text.grid(row=0, column=0, padx=10, pady=10)
        self.entry.grid(row=0, column=1, padx=10, pady=10)
        orginal_lang.grid(row=1, column=0, padx=10, pady=10)
        self.source_lang.grid(row=1, column=1, padx=10, pady=10)
        target_lang.grid(row=2, column=0, padx=10, pady=10)
        self.target_lang.grid(row=2, column=1, padx=10, pady=10)
        translate_button.grid(row=3, column=0, columnspan=2, pady=10)
        self.result_label.grid(row=4, column=0, columnspan=2, pady=10)

    def translate_text(self):
        text_to_translate = self.entry.get()

        url = f"https://translation.googleapis.com/language/translate/v2?key={api_key}" # API key in Environment Variables
        params = {
            'q': text_to_translate,
            'source': self.source_lang.get(),
            'target': self.target_lang.get(),
        }

        response = requests.post(url, params=params)
        translated_text = response.json()['data']['translations'][0]['translatedText']

        self.result_label.config(text=translated_text)

if __name__ == "__main__":

    api_key = os.environ["GOOGLE_API_KEY"]
    if api_key:
        print("API Key retrieved successfully")
    else:
        print("API Key not found")
        
    root = tk.Tk()
    app = TextTranslatorApp(root)
    root.mainloop()