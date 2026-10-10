import speech_recognition as sr
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    print("Bot:", text)
    engine.say(text)
    engine.runAndWait()

def record_audio(duration=5, fs=44100):
    print("Listening...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    wav.write("temp.wav", fs, recording)
    return "temp.wav"

def listen():
    recognizer = sr.Recognizer()
    audio_file = record_audio()

    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You:", text)
        return text
    except:
        return ""

while True:
    user_input = listen()

    if "hello" in user_input.lower():
        speak("Hello Deepu, how are you?")
    elif "your name" in user_input.lower():
        speak("I am your Python voice assistant.")
    elif "bye" in user_input.lower():
        speak("Goodbye Deepu!")
        break
    else:
        speak("I did not understand.")