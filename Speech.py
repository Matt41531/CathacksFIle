
import json
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
        print("Say something")
        print("done")
        while done == False:

            audio = r.listen(source)
            try:
                text = r.recognize_google(audio)
                print(text)
                results = sentiment_analyze(text)
                resultsj = json.loads(results)
                #print(resultsj)
                score=resultsj["keywords"][0]["sentiment"]["score"]
                print(score)
                if score < -.6:
                    print("YOU ARE BANNED")

                if r.recognize_google(audio) == "done":
                    done = True

            except:
                pass

        print("exit")


def main():
    speech_to_text()

main()