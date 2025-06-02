# Get weather by city name (OpenWeatherMap API key needed).

import requests

city = "London"
api_key = "your_api_key"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

data = requests.get(url).json()
print(f"{city}: {data['main']['temp']}°C, {data['weather'][0]['description']}")
