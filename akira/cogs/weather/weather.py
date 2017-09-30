from pyowm import OWM


def get_weather(place):
    api_key = '8338971e5cabf63215b9b3fd5f34f5a3'
    owm = OWM(api_key)
    owm_en = OWM()

    current = owm.weather_at_place(place)
    temp = current.get_weather().get_temperature('fahrenheit')
    status = current.get_weather().get_detailed_status()
    daily_forecasts = owm.daily_forecast(place).get_forecast()

    for forecast in daily_forecasts:
        date = forecast.get_reference_time('iso')
        current = forecast.get_status()
        temperature = forecast.get_temperature('fahrenheit')

        print(date, current, temperature)

    return temp, current, daily_forecasts, status


def get_zip_weather(zip_code):
    api_key = '8338971e5cabf63215b9b3fd5f34f5a3'
    owm = OWM(api_key)
    owm_en = OWM()

    #Initialize 
    current = owm.weather_at_zip_code(zip_code)
    temp = current.get_weather().get_temperature('fahrenheit')
    status = current.get_weather().get_detailed_status()
    daily_forecasts = owm.daily_forecast(zip_code).get_forecast()

    return temp, current, daily_forecasts, status


def parse_temp(temp):
    cur_temp = str(temp['temp'])
    max_temp = str(temp['temp_max'])
    min_temp = str(temp['temp_min'])

    return cur_temp, max_temp, min_temp

def parse_forecast(forecast):
    description = str(forecast[''])

