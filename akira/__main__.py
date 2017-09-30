__version__ = '0.0.1'

import os
from voice import tts
from cogs import duck_search, weather, twitter
import pocketsphinx
import pyaudio

p = pyaudio.PyAudio()
stream = p.open(
   format=pyaudio.paInt16,
   channels=1,
   rate=16000,
   input=True,
   frames_per_buffer=20480)
stream.start_stream()

def wait_for_hotword():
    pocketsphinx_dir = os.path.dirname(pocketsphinx.__file__)
    model_dir = os.path.join(pocketsphinx_dir, 'model')
    config = pocketsphinx.Decoder.default_config()
    config.set_string('-hmm', os.path.join(model_dir, 'en-us'))
    config.set_string('-keyphrase', 'hello')
    config.set_string('-dict', os.path.join(model_dir, 'cmudict-en-us.dict'))
    config.set_float('-kws_threshold', 1e-8)
    decoder = pocketsphinx.Decoder(config)

    decoder.start_utt()

    while True:
        buf = stream.read(1024)
        if buf:
            decoder.process_raw(buf, False, False)
            if decoder.hyp() is not None:
                decoder.end_utt()
                return True


def main():
    tts("Starting up akira.")

    while wait_for_hotword():
        tts("received hotword")
        #weather.run()

if __name__ == '__main__':
    main()
