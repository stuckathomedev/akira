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
    cur_temp = str(temp['temp'])
    max_temp = str(temp['temp_max'])
    min_temp = str(temp['temp_min'])

    return cur_temp, max_temp, min_temp


trigger_regex = re.compile("^(what's the weather|what is the weather|weather).+$", re.IGNORECASE + re.UNICODE)

def run():
    temp, current, daily_forecasts, status = get_zip_weather("01720")
    cur_temp, max_temp, min_temp = parse_temp(temp)
    tts(f"The temperature today is {cur_temp} degrees Fahrenheit, with a high of {max_temp} degrees and a low of {min_temp}. The current forecast is {status}.")
