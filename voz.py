import speech_recognition as sr
 
def callback(recognizer, audio):
    # received audio data, now we'll recognize it using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        texto = recognizer.recognize_google(audio,language="es-PE")
        #print("Has dicho, " + texto)
        s.send(texto.encode())
    except sr.UnknownValueError:
        #print('No entiendo.')
        s.send(b"No entiendo.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        #s.send("No se reciben datos del servicio de reconocimiento de voz.")  
#s.close() 
r = sr.Recognizer()
m = sr.Microphone()
with m as source:
    r.adjust_for_ambient_noise(source) # we only need to calibrate once, before we start listening
 
# start listening in the background (note that we don't have to do this inside a `with` statement)
stop_listening = r.listen_in_background(m, callback)
# `stop_listening` is now a function that, when called, stops background listening
 