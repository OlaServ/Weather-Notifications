from dotenv import load_dotenv
import requests


class Location:
    def __init__(self):
        self.city = self.get_user_location()

    def get_user_location(self):
        load_dotenv()

        city = requests.get("https://ipinfo.io/json").json()["city"]

        return city

