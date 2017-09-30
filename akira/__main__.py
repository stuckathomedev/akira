__version__ = '0.0.1'

import os, math, time, re
from voice import tts
from cogs import duck_search, weather, twitter
import pocketsphinx
import pyaudio
import speech_recognition as sr

p = pyaudio.PyAudio()
stream = p.open(
   format=pyaudio.paInt16,
   channels=1,
   rate=16000,
   input=True,
   frames_per_buffer=20480)
stream.start_stream()

pocketsphinx_dir = os.path.dirname(pocketsphinx.__file__)
model_dir = os.path.join(pocketsphinx_dir, 'model')
config = pocketsphinx.Decoder.default_config()
config.set_string('-hmm', os.path.join(model_dir, 'en-us'))
config.set_string('-keyphrase', 'hello')
config.set_string('-dict', os.path.join(model_dir, 'cmudict-en-us.dict'))
config.set_float('-kws_threshold', math.pow(10, -12))
decoder = pocketsphinx.Decoder(config)

def wait_for_hotword():
    decoder.start_utt()

    while True:
        buf = stream.read(1024, exception_on_overflow=False)
        if buf:
            decoder.process_raw(buf, False, False)
            if decoder.hyp() is not None:
                decoder.end_utt()
                return True


def main():
    tts("Starting up akira.")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        while wait_for_hotword():
            tts("Hi!")
            audio = r.listen(source)
            try:
                statement = str(r.recognize_google(audio))
            except:
                tts("Sorry, please try again.")
                continue
            statement = re.sub('^(hi |hello )', '', statement)
            tts(statement)

            time.sleep(1)

        #weather.run()

if __name__ == '__main__':
    main()
