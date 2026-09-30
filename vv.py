import requests
from datetime import datetime

response = requests.get(
    "https://api.open-meteo.com/v1/forecast?latitude=31.56&longitude=74.33&hourly=temperature_2m"
)

data = response.json()

temp = data["hourly"]["temperature_2m"]
time = data["hourly"]["time"]

for i in range(1, 20):
    readable_time = datetime.fromisoformat(time[i]).strftime("%d %b, %I:%M %p")

    print(
        "Temperature:", round(temp[i], 1), "°C",
        "Time:", readable_time
    )
