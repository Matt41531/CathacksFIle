
import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Say something")
    audio = r.listen(source)
    print("done")

try:
    print("Google thinks you said " + r.recognize_google(audio))

except:
    pass

