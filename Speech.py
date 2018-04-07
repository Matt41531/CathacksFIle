
import json
import speech_recognition as sr
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 \
  import Features, EntitiesOptions, KeywordsOptions

def sentiment_analyze():
    natural_language_understanding = NaturalLanguageUnderstandingV1(
         url="https://gateway.watsonplatform.net/natural-language-understanding/api",
         username= "e876778c-b8b8-4cc1-bac2-475198931406",
         password= "NNFyyadwzKwB",
         version = '2018-03-16')

    response = natural_language_understanding.analyze(
      text='IBM is an American multinational technology company '
           'headquartered in Armonk, New York, United States, '
           'with operations in over 170 countries.',
      features=Features(
        entities=EntitiesOptions(
          emotion=True,
          sentiment=True,
          limit=2),
        keywords=KeywordsOptions(
          emotion=True,
          sentiment=True,
          limit=2)))

    print(json.dumps(response, indent=2))

def analyze_text(text):
    negative = False
    words = text.split()
    for word in words:
        with open("negative_text.txt") as openfile:
            for line in openfile:
                for part in line.split():
                    if word == part:
                        print(word + " was negative")
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
    sentiment_analyze()
    speech_to_text()

main()