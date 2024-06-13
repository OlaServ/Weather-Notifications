# Weather Notification App

This Weather Notification App fetches the current weather information for a specified location and displays notifications at regular intervals. The app uses the `requests` library to fetch weather data from an API and the `win11toast` library to display notifications on Windows. It also allows the user to input a new location through a dialog box. The default location is based on the device's IP address. 

## Features

- Fetches and displays the current weather information for a specified location.
- Periodically shows weather notifications every 20 minutes.
- Allows the user to change the location via an input dialog.
- Handles errors gracefully and prompts the user to enter a correct location if an error occurs.

## Requirements

- Python 3.x
- `requests` library
- `python-dotenv` library
- `win11toast` library
- `easygui` library

## Installation

1. **Clone the repository** or download the source code.

2. **Install the required libraries**:
   ```bash
   pip install requests python-dotenv win11toast easygui 
