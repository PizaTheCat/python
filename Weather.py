# weather
# https://github.com/csparpa/pyowm
# https://openweathermap.org/appid
# e35813ecf6df5c648a2f3c69c2c700bb
# 1330050f05c5c2c1f05e678136d1ebc2
# pip instally pyowm
place = 'Sydney'
import pyowm
owm = pyowm.OWM('1330050f05c5c2c1f05e678136d1ebc2')  # You MUST provide a valid API key
observation = owm.weather_at_place(place)

# Have a pro subscription? Then use:
# owm = pyowm.OWM(API_key='your-API-key', subscription_type='pro')

# Will it be sunny tomorrow at this time in Milan (Italy) ?
forecast = owm.daily_forecast("Sydney, AU")
tomorrow = pyowm.timeutils.tomorrow()
forecast.will_be_sunny_at(tomorrow)  # Always True in Italy, right? ;-)

# Search for current weather in London (UK)
# observation = owm.weather_at_place('London,uk')
w = observation.get_weather()
# print(observation.get_weather()) # <Weather - reference time=2013-12-18 09:20,                              # status=Clouds>

# Weather details

# Search current weather observations in the surroundings of
# lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
# print(observation_list)
# Find observed weather in all the "London"s in the world

# Find observed weather for all the places in the surroundings of lon=-2.15,lat=57
# obs_list = owm.weather_around_coords(-2.15, 57)
# print(owm.weather_around_coords(-2.15, 57))
# # As above but limit result items to 8
# obs_list = owm.weather_around_coords(-2.15, 57, limit=8)
# print(owm.weather_around_coords(-2.15, 57, limit=8))
# You can retrieve the Weather object like this:


# and then access weather data using the following methods:

w.get_reference_time()                             # get time of observation in GMT UNIXtime
print("Time of data collection: " + str(w.get_reference_time(timeformat='iso')))
w.get_reference_time(timeformat='iso')             # ...or in ISO8601
print("Date of data collection: " + str(w.get_reference_time(timeformat='date')))
# print(w.get_reference_time(timeformat='iso'))
# w.get_reference_time(timeformat='date')            # ...or as a datetime.datetime object
# print(w.get_reference_time(timeformat='date'))

w.get_clouds()                                      # Get cloud coverage
print("Clouds: " + str(w.get_clouds()))

w.get_rain()                                       # Get rain volume
print("Rain: " + str(w.get_rain()))
#
# w.get_snow()                                       # Get snow volume
# print(w.get_snow())
print("Wind: " + str(w.get_wind()))
w.get_humidity()                                   # Get humidity percentage
print("Humidity: " + str(w.get_humidity()) + "%")

w.get_pressure()                                   # Get atmospheric pressures
print("Pressure: " + str(w.get_pressure()))

# w.get_temperature()                                # Get temperature in Kelvin
# {'temp': 293.4, 'temp_kf': None, 'temp_max': 297.5, 'temp_min': 290.9}
# print(w.get_temperature())
w.get_temperature(unit='celsius')                  # ... or in Celsius degs
print("Temperature: " + str(w.get_temperature(unit='celsius')))
# w.get_temperature('fahrenheit')                    # ... or in Fahrenheit degs
# print("Temperature"w.get_temperature(unit='fahrenheit'))
# w.get_status()                                     # Get weather short status
# 'clouds'
# print(w.get_status())
w.get_detailed_status()                           # Get detailed weather status
'Broken clouds'
print("Weather Status: " + str(w.get_detailed_status()))
# w.get_weather_code()                               # Get OWM weather condition code
# print(w.get_weather_code())
#
# w.get_weather_icon_name()                          # Get weather-related icon name

# print(w.get_weather_icon_name())
w.get_sunrise_time()                               # Sunrise time (GMT UNIXtime or ISO 8601)
print("Sunrise Time: " + str(w.get_sunrise_time('iso')))
w.get_sunset_time('iso')                           # Sunset time (GMT UNIXtime or ISO 8601)

print("Sunset Time: " + str(w.get_sunset_time('iso')))
