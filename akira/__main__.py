__version__ = '0.0.1'

import os, math, time, re
from voice import tts
from modules import duck_search, weather, twitter, quit as leave, facebook, matrix, journal, challenges
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
    r.non_speaking_duration = 0.5
    r.pause_threshold = 0.5
    while wait_for_hotword():
        with sr.Microphone() as source:
            tts("Hey!")
            audio = r.listen(source)
            try:
                print("dbg: waiting for speech recognition")
                statement = str(r.recognize_google(audio))
                print("dbg: got speech recognition")

                statement = re.sub('^(hi|hello|please|hey|akira)', '', statement).strip()
                found_module = False
                for module in [leave, duck_search, twitter, weather, facebook, matrix, journal, challenges]:
                    print("dbg: testing module " + str(module))
                    if module.trigger_regex.match(statement):
                        print(f"dbg: starting {module}")
                        found_module = True
                        print(f"dbg: found match: {module.trigger_regex.match(statement)}")
                        module.run(module.trigger_regex.match(statement))
                if not found_module:
                    tts(f"Sorry, I'm not sure what you meant by '{statement}'.")
            except sr.UnknownValueError:
                tts("Sorry, I didn't catch that.")
            except sr.RequestError:
                tts("Sorry, speech recognition failed. Please check your internet connection.")

            time.sleep(2)

if __name__ == '__main__':
    main()
