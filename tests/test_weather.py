import requests_mock
import pytest
from unittest.mock import patch
from weather import Weather


class TestWeather:

    def setup_method(self):
        self.mock_response = {
            "current": {
                "temp_c": 7,
                "condition": {
                    "text": "Partly cloudy",
                    "icon": "//icon.png"
                }
            }
        }

        self.new_mock_response = {
            "current": {
                "temp_c": 20,
                "condition": {
                    "text": "Sunny",
                            "icon": "//sunny.png"
                }
            }
        }
        self.location = "Berlin"

        self.new_location = "New York"

        self.mock_error_response = {"error": {"code": 1006,
                                              "message": "No matching location found."}}

        self.api_key = "test_key"

    @pytest.fixture
    def weather(self):
        with requests_mock.Mocker() as m:
            m.get("http://api.weatherapi.com/v1/current.json",
                  json=self.mock_response)
            weather_instance = Weather(
                city=self.location, api_key=self.api_key)
            return weather_instance

    def test_get_weather(self, weather):

        assert weather.temperature == 7
        assert weather.condition == "Partly cloudy"
        assert weather.location == self.location
        assert weather.icon == "https://icon.png"

    def test_weather_invalid_city(self):

        with requests_mock.Mocker() as m:
            m.get("http://api.weatherapi.com/v1/current.json",
                  json=self.mock_error_response, status_code=400)

            with pytest.raises(KeyError):
                weather = Weather(city="invalid_location",
                                  api_key=self.api_key)
                assert weather.complete_weather == None
                assert weather.condition == None
                assert weather.temperature == None
                assert weather.ion == None

                with patch("weather.show_dialog") as mock_show_dialog:
                    mock_show_dialog.assert_called()

    def test_show_notification(self, weather):
        assert weather.location == self.location

        with patch('tkinter.simpledialog.askstring', return_value=self.new_location):
            with requests_mock.Mocker() as m:

                m.get("http://api.weatherapi.com/v1/current.json",
                      json=self.new_mock_response)
                with patch.object(weather, 'show_notification') as mock_show_notification:
                    weather.show_dialog()
                    assert weather.location == self.new_location
                    assert weather.temperature == 20
                    assert weather.condition == "Sunny"
                    assert weather.icon == "https://sunny.png"
                    mock_show_notification.assert_called()
