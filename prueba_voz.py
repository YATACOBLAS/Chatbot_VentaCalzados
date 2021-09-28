#pip iinstall pyttsx3
#pip install mysql.connector
#pip install pipwin
#pipwin install pyaudio

import pyttsx3
import speech_recognition as sr
import mysql.connector
from difflib import SequenceMatcher as SM 
import random
import time

recognizer=sr.Recognizer()

microphone=sr.Microphone(device_index=0)
eng=pyttsx3.init()

#configurar la velocidad de pronucniancion
eng.setProperty("rate",160)
#establecer con le volumen de la voz
eng.setProperty("volumen",1.0)
#Establecemos la voz ah utilizar 

listVoices=eng.getProperty("voices")
eng.setProperty("voice",listVoices[0].id)

eng.say("Hola que tal Jefe,estoy listo para trabajar")
eng.runAndWait() 

def recognizeMicAudio():
	palabra =""
	print("Escuchando...")
	with microphone as source:
	    audio=recognizer.listen(source)
	    palabra=recognizer.recognize_google(audio,language="es-PE")
	    return palabra

print(recognizeMicAudio())