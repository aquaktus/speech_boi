#!/usr/local/bin/python3
import speech_recognition as sr
import argparse
from os import system
import time
from pyfiglet import Figlet
print("Using Speech Recogniser version:", sr.__version__)

parser = argparse.ArgumentParser()

parser.add_argument("--speech_recogniser", help="folder location to save the trained model", default="sphinx")
parser.add_argument("--phrase_time_limit", type=float, help="folder location to save the trained model", default=5)


F = Figlet(font='slant')
print(F.renderText(' Speech Boi !!!'))
print("                The Voice Adventure!")
print("")
print("                    By Carlos Gemmell")
print("")
print("")
print("")

with open('CREDENTIAL JSON FILE HERE', 'r') as myfile:
    creds=myfile.read()

r = sr.Recognizer()
mic = sr.Microphone()
text = "> "

def listen_and_recognise(mic, r):
    with mic as source:
        print("Listening to audio...")
        start_listen = time.time()
        r.adjust_for_ambient_noise(source, duration=0.5)
        #audio = r.listen(source, phrase_time_limit=6)
        audio = r.listen(source,phrase_time_limit=20)
        end_listen = time.time()
        print("Done listening to Audio:", end_listen - start_listen)
        #text = r.recognize_google_cloud(audio, credentials_json=creds)
        start_transcribe = time.time()
        text = r.recognize_sphinx(audio)
        end_transcribe = time.time()
        print("Transcription in:", end_transcribe - start_transcribe)
        print(">", text)
        return text

def regognise_on_press(mic, r):
    text = input("Press Enter to use voice or type: ")
    if text == "":
        text = listen_and_recognise(mic, r)
    return text

def say(text):
    print("Reconstructing voice")
    system("say " + text.replace("'","\\'"))
    # spawnl(os.P_NOWAIT, "say " + text.replace("'","\\'"))

# with mic as source:
#     while True:
#         # r.adjust_for_ambient_noise(source, duration=0.5)
#         # audio = r.listen(source, phrase_time_limit=6)
#         audio = r.listen(source,phrase_time_limit=2)
#         # print("Done listening to Audio")
#         # print("Output:")
#         text = text + r.recognize_sphinx(audio)
#         print(text, end="\r")

# with mic as source:
#     print("Listening to audio...")
#     r.adjust_for_ambient_noise(source, duration=0.5)
#     #audio = r.listen(source, phrase_time_limit=6)
#     audio = r.listen(source,phrase_time_limit=20)
#     print("Done listening to Audio")

text = regognise_on_press(mic, r)

responce_text = "Look Carlos, I do not want to deal with your shit again"

say(text)
