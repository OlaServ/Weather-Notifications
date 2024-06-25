from weather import Weather
from location import Location
import os
from dotenv import load_dotenv
import threading


load_dotenv()
api_key = os.getenv('API_KEY')

city = Location().city
weather = Weather(city=city, api_key=api_key)

def periodic_notification():
    weather.show_notification()
    threading.Timer(1200, periodic_notification).start()


periodic_notification()