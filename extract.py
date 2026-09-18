import requests
import pandas as pd

# Free API, no key required — hourly weather for a fixed location
url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 6.68,       # Ratnapura, Sri Lanka
    "longitude": 80.40,
    "hourly": "temperature_2m,relative_humidity_2m,precipitation",
    "past_days": 7
}

response = requests.get(url, params=params)
response.raise_for_status()   # crash loudly if the API call failed
data = response.json()

df = pd.DataFrame(data["hourly"])
df.to_csv("raw_weather.csv", index=False)
print(f"Saved {len(df)} rows to raw_weather.csv")