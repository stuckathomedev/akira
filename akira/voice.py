import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 150)  #120 words per minute
engine.setProperty('volume', 0.9)
engine.setProperty('voice', 'english-north')


def tts(message):
    engine.say(message)
    print(f"tts: {message}")
    engine.runAndWait()
