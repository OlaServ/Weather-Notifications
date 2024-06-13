import os
from dotenv import load_dotenv
import requests
from win11toast import toast
from location import Location
import easygui
import time


class Weather:
    def __init__(self):
        self.location = Location().city
        self.complete_weather = self.get_weather()
        self.temperature, self.condition, self.icon = self.parse_weather()

    load_dotenv()

    api_key = os.getenv('API_KEY')

    url = "http://api.weatherapi.com/v1/current.json"

    def get_weather(self):
        r = requests.get(self.url, params={
                         "key": self.api_key, "q": self.location})
        return r.json()

    def parse_weather(self):
        icon_url = "https:" + \
            self.complete_weather["current"]["condition"]["icon"]

        temperature = self.complete_weather["current"]["temp_c"]
        condition = self.complete_weather["current"]["condition"]["text"]
        icon = icon_url

        return temperature, condition, icon

    def show_dialog(self, _=None, message="Type your location"):
        user_input = easygui.enterbox(msg=message)
        if len(user_input) > 0:
            try:
                self.location = user_input
                self.complete_weather = self.get_weather()
                self.temperature, self.condition, self.icon = self.parse_weather()
                self.show_notification()
            except KeyError:
                self.show_dialog(self, message="Enter correct location")

    def show_notification(self):
        toast(f"Weather in {self.location}",
              f"Temperature: {self.temperature}C \n{self.condition}", icon=self.icon, on_click=self.show_dialog, button='Change location')


weather = Weather()

while True:
    weather.show_notification()
    time.sleep(1200)
