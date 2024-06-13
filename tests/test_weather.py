import requests_mock
from weather import Weather

    
def test_weather():
    location = "Berlin"  
    
    mock_response = {
        "current": {
            "temp_c": 7,
            "condition": {
                "text": "Partly cloudy",
                "icon": "icon.png"
            }
        }
    }
    
    with requests_mock.Mocker() as m:
        m.get("http://api.weatherapi.com/v1/current.json", json=mock_response)
        
        weather = Weather(city=location, api_key="test_key")
        
        assert weather.complete_weather["current"]["temp_c"] == 7
        assert weather.complete_weather["current"]["condition"]["text"] == "Partly cloudy"