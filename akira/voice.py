import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 165)
engine.setProperty('volume', 0.5)
engine.setProperty('voice', 'english-north')


def tts(message):
    engine.say(message)
    print(f"tts: {message}")
    engine.runAndWait()
