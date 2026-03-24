import requests

city = input("Введите город: ")

url = "https://api.openweathermap.org/data/2.5/weather"
params = {
    "q": city,
    "units": "metric",
    "lang": "ru",
    "appid": "79d1ca96933b0328e1c7e3e7a26cb347"
}

response = requests.get(url, params=params)
data = response.json()

if response.status_code != 200:
    print("Ошибка:", data.get("message", "неизвестная ошибка"))
else:
    temp = round(data["main"]["temp"])
    feels_like = round(data["main"]["feels_like"])
    pressure = data["main"]["pressure"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    description = data["weather"][0]["description"]

    print(f"\nПогода в городе {city}:")
    print(f"Температура: {temp} °C")
    print(f"Ощущается как: {feels_like} °C")
    print(f"Ветер: {wind_speed} м/с")
    print(f"Давление: {pressure} гПа")
    print(f"Влажность: {humidity}%")
    print(f"На небе: {description}")
