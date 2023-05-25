import speech_recognition as sr
import pyttsx3 as audio
import requests

API_KEY = ""

class MainService():
    def __int__(self):
        pass;

    def getText(self) -> str:
        rec = sr.Recognizer()
        with sr.Microphone(device_index=1) as mic:
            rec.adjust_for_ambient_noise(mic)
            print("Escutando...")
            audio = rec.listen(mic)
            return rec.recognize_google(audio, language="pt-BR")

    def getAudio(self, text):
        engine = audio.init()
        engine.say(text)
        engine.runAndWait()

    def makeQuestion(self, text) -> str:
        url = "https://api.openai.com/v1/completions"
        headers = {
            "Authorization": "Bearer " + API_KEY,
            "Content-Type": "application/json"
        }

        data = {
            "model": "text-davinci-001",
            "prompt": text,
            "temperature": 1,
            "max_tokens": 1024
        }
        response = requests.post(url, headers=headers, json=data)
        resultado = response.json()
        return resultado['choices'][0]['text']
