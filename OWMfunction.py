# https://github.com/csparpa/pyowm
# https://openweathermap.org/appid
# e35813ecf6df5c648a2f3c69c2c700bb
# 1330050f05c5c2c1f05e678136d1ebc2
# pip instally pyowm
# Look at Weather.py for reference
from printName import printGlenn
import pyowm
import datetime
printGlenn()
owm = pyowm.OWM('1330050f05c5c2c1f05e678136d1ebc2')  # You MUST provide a valid API key
def weatherforcast( place ):
    tomorrow = pyowm.timeutils.tomorrow()
    observation = owm.weather_at_place(place)
    forecast = owm.daily_forecast(place)
    forecast.will_be_sunny_at(tomorrow)
    w = observation.get_weather()
    print("Time is at GMT +00")
    print("Sunny Tomorrow? True / False: " + str(forecast.will_be_sunny_at(tomorrow)))
    print("Time of data collection: " + str(w.get_reference_time(timeformat='iso')))
    print("Clouds: " + str(w.get_clouds()))
    print("Wind: " + str(w.get_wind()))
    print("Humidity: " + str(w.get_humidity()) + "%")
    print("Pressure: " + str(w.get_pressure()))
    print("Temperature: " + str(w.get_temperature(unit='celsius')))
    print("Weather Status: " + str(w.get_detailed_status()))
    print("Sunrise Time: " + str(w.get_sunrise_time('iso')))
    print("Sunset Time: " + str(w.get_sunset_time('iso')) + "                                                                                                                                       ")
    def fileWrite():
        f = open("owmRecords.txt")
        with open("owmRecords.txt",'a',encoding = 'utf-8') as f:
            f.write("City: ")
            f.write(str(inputA) + "\n")
            f.write("Sunny Tomorrow? True / False: ")
            f.write(str(forecast.will_be_sunny_at(tomorrow)) + "\n")
            f.write("Time of data collection: ")
            f.write(str(w.get_reference_time(timeformat='iso')) + "\n")
            f.write("Time now: ")
            f.write(str(datetime.datetime.now()) + "\n")
            f.write("Clouds: ")
            f.write(str(w.get_clouds()) + "\n")
            f.write("Wind: ")
            f.write(str(w.get_wind()) + "\n")
            f.write("Humidity: ")
            f.write(str(w.get_humidity()) + "%" + "\n")
            f.write("Pressure: ")
            f.write(str(w.get_pressure()) + "\n")
            f.write("Temperature: ")
            f.write(str(w.get_temperature(unit='celsius')) + "\n")
            f.write("Weather Status: ")
            f.write(str(w.get_detailed_status()) + "\n")
            f.write("Sunrise Time: ")
            f.write(str(w.get_sunrise_time('iso')) + "\n")
            f.write("Sunset Time: ")
            f.write(str(w.get_sunset_time('iso')) + "\n" + "\n" + "\n")
    fileWrite()
inputA = input("Please input the requested city: ")
weatherforcast(inputA)
