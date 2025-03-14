import pygame
from threading import Timer
import time
import os
from tkinter import filedialog
import pyttsx3
import speech_recognition as sr



song = []
directory = filedialog.askdirectory()
for root, dirs, files in os.walk(directory):
    for file in files:
        if os.path.splitext(file)[1] == '.mp3':
            path = (root + '/' + file).replace('\\', '/')
            song.append(path)

pygame.mixer.init()
pygame.mixer.music.load(song[0])
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
rate = engine.setProperty('rate', 125)
listener = sr.Recognizer()
si = 0

def take_command():
    global si
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()

            if 'savannah' in command:
                engine.say('hi i am savannah ,your assistant only developed to play music')
                engine.runAndWait()

            elif 'play' in command:
                engine.say('okay,music will play in few seconds')
                engine.runAndWait()
                pygame.mixer.music.play()

            elif 'stop' in command:
                pygame.mixer.music.stop()
                engine.say('okay ,music is stopped')
                engine.runAndWait()

            elif 'pause' in command:
                pygame.mixer.music.pause()
                engine.say('music is paused')
                engine.runAndWait()

            elif 'resume' in command:
                engine.say('okay music is gonna resume')
                engine.runAndWait()
                time.sleep(2)
                pygame.mixer.music.unpause()

            elif 'next song' in command:
                try:
                    si += 1
                    pygame.mixer.music.load(song[si])
                    pygame.mixer.music.play()
                except:
                    print("This is the last song")

            elif 'previous song' in command:
                try:
                    si -= 1
                    pygame.mixer.music.load(song[si])
                    pygame.mixer.music.play()
                    print(prev_song)
                except:
                    print("This is the first song")

            elif 'increase volume' in command:
                print('Enter the volume (value between 0.1 to 1.0):')
                n = float(input())
                pygame.mixer.music.set_volume(n)

            elif 'decrease volume' in command:
                pygame.mixer.music.pause()
                print('Please tell rate of volume in the format of increase volume upto volume')
                n = input()
                a = n.split()
                b = a[-1]
                g = float(b)
                v = g / 100
                pygame.mixer.music.set_volume(v)
                pygame.mixer.music.play()

            else:
                engine.say('sorry,i am only developed to play music , not other tasks')
                engine.runAndWait()

            Timer(1, take_command).start()
    except:
        print("I don't understand anything")


take_command()
