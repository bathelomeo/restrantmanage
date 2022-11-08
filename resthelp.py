import speech_recognition as sr
import pyaudio

r = sr.Recognizer()

with sr.Microphone() as source:
    print('May i take your order?')
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print('Cook Le : {}'.format(text))
    except:
        print('Sorry I could not hear you, Please repeat')