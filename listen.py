import speech_recognition as sr
import os
import threading
from mtranslate import translate


def translation_hin_to_eng(text):
    english_translation = translate(text, 'en-in')
    return english_translation


def print_loop():
    while True:
        print("", end='', flush=True)

def hearing():
    language = "hi"
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = False
    recognizer.energy_threshold = 9000  # Adjust this threshold based on your environment

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=None)
            recognized_text = recognizer.recognize_google(audio).lower()  # Convert to lowercase

            if recognized_text:
                translated_text = translation_hin_to_eng(recognized_text)
                print("Mr.Stank: " + translated_text)
                return translated_text  # Return the translated text
            else:
                return ""  # Return an empty string if no speech is recognized
        except sr.UnknownValueError:
            return ""

