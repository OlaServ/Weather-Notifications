import requests
from win11toast import toast
from tkinter import simpledialog


class Weather:
    def __init__(self, city, api_key):
        self.api_key = api_key
        self.location = city
        self.temperature = None
        self.icon = None
        self.condition = None
        self.get_weather()

    url = "http://api.weatherapi.com/v1/current.json"

    def get_weather(self):
        r = requests.get(self.url, params={
                         "key": self.api_key, "q": self.location})
        parsed_response = r.json()
        self.temperature = parsed_response["current"]["temp_c"]
        self.condition = parsed_response["current"]["condition"]["text"]
        self.icon = "https:" + \
            parsed_response["current"]["condition"]["icon"]

    def show_dialog(self, _=None, message="Type your location"):
        user_input = simpledialog.askstring("Location Input", message)
        if user_input:
            try:
                self.location = user_input
                self.get_weather()
                self.show_notification()

            except KeyError:
                self.show_dialog(self, message="Enter correct location")

    def show_notification(self):
        toast(f"Weather in {self.location}",
              f"Temperature: {self.temperature}C \n{self.condition}", icon=self.icon, on_click=self.show_dialog, button='Change location')
