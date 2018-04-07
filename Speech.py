
import speech_recognition as sr

def analyze_text(text):
    words = text.string()
    for word in words:
        print(word)
    return words


def speech_to_text():
    r = sr.Recognizer()
    done = False
    with sr.Microphone() as source:
        print("Say something")
        print("done")
        while done == False:

            audio = r.listen(source)
            try:
                text = r.recognize_google(audio)
                print(text)
                words = analyze_text(text)
                for word in words:
                    print(word + ",")
                if r.recognize_google(audio) == "done":
                    done = True

            except:
                pass

        print("exit")


def main():
    speech_to_text()

main()