#THIS PROGRAMM WAS WRITTEN BY mthudaa or M. Taufiqul Huda#
import speech_recognition as sr
import pyttsx3 as speak

listener = sr.Recognizer()
engine = speak.init()


def bicara(text):
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()

def dengar():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            command = command.replace('computer', '')
    except:
        pass
    return command

def init():
    text = dengar()
    print(text)
    bicara(text)
while(True):
    init()
