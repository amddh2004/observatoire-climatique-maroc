import requests
import pandas as pd
URL = "https://archive-api.open-meteo.com/v1/archive"
params = {
    "latitude": 34.0209,          # Rabat
    "longitude": -6.8416,
    "start_date": "2026-10-01",
    "end_date": "2026-10-31",
    "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum,wind_speed_10m_max",
    "timezone": "Africa/Casablanca",
}
response = requests.get(URL, params=params, timeout=30)
response.raise_for_status()
data = response.json()

print("Clés du JSON :", list(data.keys()))
print("Unités :", data["daily_units"])

df = pd.DataFrame(data["daily"])
df["ville"] = "Rabat"
print(df.head())
print(df.shape)
print(df.dtypes)