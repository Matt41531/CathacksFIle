
import speech_recognition as sr

def analyze_text(text):
    negative = False
    words = text.split()
    for word in words:
        with open("negative_text.txt") as openfile:
            print("Opened")
            for line in openfile:
                for part in line.split():
                    if word == part:
                        print("That was negative")
                        negative = True
    return negative


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
                negative_words_found = analyze_text(text)
                if negative_words_found:
                    print("YOU ARE BANNED")

                if r.recognize_google(audio) == "done":
                    done = True

            except:
                pass

        print("exit")


def main():
    speech_to_text()

main()