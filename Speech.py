
import json
import speech_recognition as sr
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 \
  import Features, EntitiesOptions, KeywordsOptions

import pyaudio
import wave

def record():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = 5
    WAVE_OUTPUT_FILENAME = "output.wav"

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


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
        while done == False:

            audio = r.listen(source)
            try:
                text = r.recognize_google(audio)
                print(text)
                results = sentiment_analyze(text)
                resultsj = json.loads(results)
                score=resultsj["keywords"][0]["sentiment"]["score"]
                print(score)
                if score < -.6:
                    print("Your speech has been determined to be negative. Please refrain from continuously adding negativity to the game.")

                if r.recognize_google(audio) == "done":
                    done = True

            except:
                pass

        print("exit")


def main():
    speech_to_text()

main()