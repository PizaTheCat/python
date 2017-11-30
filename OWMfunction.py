# https://github.com/csparpa/pyowm
# https://openweathermap.org/appid
# e35813ecf6df5c648a2f3c69c2c700bb
# 1330050f05c5c2c1f05e678136d1ebc2
# pip instally pyowm
import pyowm
owm = pyowm.OWM('1330050f05c5c2c1f05e678136d1ebc2')  # You MUST provide a valid API key
def weatherforcast( place ):
    observation = owm.weather_at_place(place)
    forecast = owm.daily_forecast(place)
    tomorrow = pyowm.timeutils.tomorrow()
    forecast.will_be_sunny_at(tomorrow)
    w = observation.get_weather()
    print("City: {0}".format(place))
    print("Sunny Tomorrow? True / False: " + str(forecast.will_be_sunny_at(tomorrow)))
    print("Time of data collection: " + str(w.get_reference_time(timeformat='iso')))
    print("Date of data collection: " + str(w.get_reference_time(timeformat='date')))
    print("Clouds: " + str(w.get_clouds()))
    print("Wind: " + str(w.get_wind()))
    print("Humidity: " + str(w.get_humidity()) + "%")
    print("Pressure: " + str(w.get_pressure()))
    print("Temperature: " + str(w.get_temperature(unit='celsius')))
    print("Weather Status: " + str(w.get_detailed_status()))
    print("Sunrise Time: " + str(w.get_sunrise_time('iso')))
    print("Sunset Time: " + str(w.get_sunset_time('iso')) + "                                                                                                                                       ")
weatherforcast('Singapore')
weatherforcast('Sydney')
weatherforcast('London')
weatherforcast('Zurich')
