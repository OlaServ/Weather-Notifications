from weather import Weather
from location import Location
import os
from dotenv import load_dotenv
import time


load_dotenv()
api_key = os.getenv('API_KEY')

city = Location().city
weather = Weather(city=city, api_key=api_key)
weather.show_notification()

while True:
    weather.show_notification()
    time.sleep(1200)