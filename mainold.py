import pyttsx3
from ollama import chat
from recogniseaudio import record_and_transcribe
from colorama import Fore
import webbrowser
import random
from playyoutube import *

firefox = webbrowser.get('C:/Program Files/Mozilla Firefox/firefox.exe %s')

model = "gemma3:4b"
messages = []
voice_mode = False

playlists = {"synthwave": "https://www.youtube.com/watch?v=wL8DVHuWI7Y&list=PL7HZm749YgC0M7YshtNn64_KD7_OOlxKr", "trailer":"https://www.youtube.com/watch?v=9orj6Kk1kss&list=PL7HZm749YgC2gEHHHvNkopAvkW3zhicru"}
playlists_unit = ["https://www.youtube.com/watch?v=wL8DVHuWI7Y&list=PL7HZm749YgC0M7YshtNn64_KD7_OOlxKr", "https://www.youtube.com/watch?v=9orj6Kk1kss&list=PL7HZm749YgC2gEHHHvNkopAvkW3zhicru"]

word_rate = 180

running = True

if __name__ == "__main__":
    while running:
        if voice_mode:
            me = record_and_transcribe()
        else:
            me = input(f"{Fore.CYAN}>>> ")
        
        if me == "chat mode":
            voice_mode = False
            continue
        if me == "voice mode":
            voice_mode = True
            continue

        if "rap" in me:
            word_rate = 240

        if "play some music" in me and "sad" in me:
            firefox.open(playlists["synthwave"])
            continue

        elif "play some music" in me and "calm" in me:
            firefox.open(playlists["trailer"])
            continue

        elif "play some music" in me:
            firefox.open(random.choice(playlists_unit))
            continue

        elif "open" in me: 
            messages = [
            {"role": "user", "content": me + " Give me only the url link of the platform. "}
        ]
            response = chat(model=model, messages=messages)
            firefox.open(response.message.content)
            continue

        elif "could you play me " in me:
            messages = [
            {"role": "user", "content": me + " Give me only the name of the song. "}
        ]
            response = chat(model=model, messages=messages)
            play_youtube(response.message.content)
            continue

        messages = [
            {"role": "user", "content": str(me)}
        ]
        
        response = chat(model=model, messages=messages)
        print(f"{Fore.BLUE}AI Response:", response.message.content + f"{Fore.WHITE}")
        engine = pyttsx3.Engine('')
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)  # wybierz głos
        engine.setProperty('rate', word_rate)
        
        pyttsx3.speak(response.message.content)
        engine.stop()
        word_rate = 180
        if me == "bye" or me == "quit":
            running = False


