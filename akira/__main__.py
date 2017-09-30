__version__ = '0.0.1'

from voice import tts
from cogs import duck_search, weather, twitter

def main():
    tts("Starting up akira.")
    weather.run()


if __name__ == '__main__':
    main()
