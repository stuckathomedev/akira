import re
from pyowm import OWM
from voice import tts


def get_zip_weather(zip_code):
    api_key = '4becd4f5bd426b1adc8d23b8496d7d00'
    owm = OWM(api_key)

    # Initialize weather
    current = owm.weather_at_zip_code(zip_code, "US")
    # Get the temperature
    temp = current.get_weather().get_temperature('fahrenheit')
    # Detailed status
    status = current.get_weather().get_detailed_status()
    # Get forecast
    daily_forecasts = owm.daily_forecast(zip_code).get_forecast()

    return temp, current, daily_forecasts, status


def parse_temp(temp):
    cur_temp = temp['temp']
    max_temp = temp['temp_max']
    min_temp = temp['temp_min']

    return cur_temp, max_temp, min_temp


def wear_clothes(temp, status):
    if temp <= 32:
        what_to_do = "It's less than freezing outside! Grab a jacket and some warm clothes!"
        return what_to_do
    elif 32 < temp <= 60:
        what_to_do = "It is somewhat chilly outside. Grab a jacket to take along and slightly warmer clothes."
        return what_to_do
    elif 60 < temp <= 85:
        what_to_do = "It is WARM outside! Go in your summer clothes."
        return what_to_do
    elif temp > 85:
        what_to_do="It's supremely hot outside! Be careful of staying outside for long amounts of time and remember to drink water!"
        return what_to_do


trigger_regex = re.compile("^(what's the weather|what is the weather|weather).+$", re.IGNORECASE + re.UNICODE)


def run():
    temp, current, daily_forecasts, status = get_zip_weather("01720")
    cur_temp, max_temp, min_temp = parse_temp(temp)
    answer = wear_clothes(cur_temp, status)
    tts(answer)
    tts(f"The temperature today is {cur_temp:.0f} degrees Fahrenheit, with a high of {max_temp:.0f} degrees and a low of {min_temp:.0f}. The current forecast is {status}.")
