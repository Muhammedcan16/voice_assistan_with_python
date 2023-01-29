from playsound import playsound
from datetime import datetime
import speech_recognition as sr
import webbrowser
import time
from gtts import gTTS
import random
import os


r = sr.Recognizer()

def record(ask = False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = r.listen(source)
        voice = ''
        try:
            voice = r.recognize_google(audio , language='tr-TR')
        except sr.UnknownValueError:
            speak('anlayamadım')
        except sr.RequestError:
            speak('sistem çalışmıyor')        
        return voice


def response(voice):
     
        if 'merhaba' in voice:
            speak('merhaba')
        
        if 'nasılsın' in voice:
            speak('iyiyim sen nasılsın')    
        
        if 'neler yapabiliyorsun' in voice:
            speak('Saati söyleyebilirim, Google dan arama yapabilirim,')

        if 'saat kaç' in voice:
            speak(datetime.now().strftime('%H:%M:%S'))
            print(datetime.now().strftime('%H:%M:%S')) 

        if 'arama yap' in voice:
            search = record('ne aramak istersin')
            url = 'https://google.com/search?q='+search
            webbrowser.get().open(url)
            speak(search + 'için bulduklarım')

        if 'kapat' in voice:
            speak('görüşürüz') 
            exit() 
  

def speak(string):
    tts = gTTS(text=string,lang='tr',slow=False)
    rand = random.randint(1,1000)
    file = str(rand)+'.mp3'
    tts.save(file)
    playsound(file)
    os.remove(file)

    
speak('merhaba sana nasıl yardımcı olabilirim')
while True:
    voice = record()
    if voice != '':
       voice= voice.lower()
       print(voice)
       response(voice)