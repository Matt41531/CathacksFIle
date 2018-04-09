
import json
from tkinter import *
from tkinter import ttk
import speech_recognition as sr
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 \
  import Features, EntitiesOptions, KeywordsOptions


def sentiment_analyze(speech_text):
    natural_language_understanding = NaturalLanguageUnderstandingV1(
         url="https://gateway.watsonplatform.net/natural-language-understanding/api",
         username="e876778c-b8b8-4cc1-bac2-475198931406",
         password="NNFyyadwzKwB",
         version='2018-03-16')

    response = natural_language_understanding.analyze(
      text=speech_text,
      features=Features(
        #entities=EntitiesOptions(
          #emotion=True,
          #sentiment=True,
          #limit=2),
        keywords=KeywordsOptions(
          #emotion=True,
          sentiment=True,
          limit=2)))

    #print(json.dumps(response, indent=2))
    return json.dumps(response, indent=2)


def test_analysis(text):
    results = sentiment_analyze(text)
    resultsj = json.loads(results)
    score = resultsj["keywords"][0]["sentiment"]["score"]
    print(score)

def speech_to_text():

    r = sr.Recognizer()
    done = False
    with sr.Microphone() as source:
        print("Referee started. Your speech is being monitored.")
        while done == False:

            audio = r.listen(source)
            try:
                text = r.recognize_google(audio)
               # print(text)
                results = sentiment_analyze(text)
                resultsj = json.loads(results)
                #print(resultsj)
                score=resultsj["keywords"][0]["sentiment"]["score"]
                print(score)
                if score < -.5:
                    print("Your speech has been determined to be negative. Please refrain from continuously adding negativity to the game.")
                    return 1

                if r.recognize_google(audio) == "done":
                    done = True

            except:
                pass

        print("exit")




def main():
    window = Tk()
    #window.title("Referee")
    enter_button = Button(window, text="Enter").grid(row=45, column=80, sticky=W, padx=4)
    cancel_button = Button(window, text="Cancel").grid(row=45, column=0, stick=W, padx=4)
    key = Entry(window).grid(row=30, column=40, sticky= W, padx=10, pady=10)
    frame = Frame(window)
    labelText = StringVar()
    label = Label(frame, textvariable=labelText)

    labelText.set("key")
    label.grid(row=0, column=40, sticky=W, padx=4)
    frame.grid()

    window.mainloop()

    running = 1
    speech_to_text()
    running = 0

main()