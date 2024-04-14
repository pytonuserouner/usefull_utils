from gtts import gTTS
import os


"""
Текст в речь. Библиотека gTTS использует гугловские технологии конвертации текста в речь.
"""


file = open("abc.txt", "r").read()

speech = gTTS(text=file, lang='en', slow=False)
speech.save("voice.mp3")
os.system("voice.mp3")