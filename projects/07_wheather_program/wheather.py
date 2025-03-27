import requests

def get_weather(city_name):
    try:
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1&language=en&format=json"
        geo_response = requests.get(geo_url).json()

        if "results" not in geo_response:
            print("❌ Error: Invalid city name. Please try again.")
            return

        lat = geo_response["results"][0]["latitude"]
        lon = geo_response["results"][0]["longitude"]

        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        weather_response = requests.get(weather_url).json()

        weather = weather_response["current_weather"]

        temperature = weather["temperature"]
        wind_speed = weather["windspeed"]
        condition = weather["weathercode"]

        print(f"\n🌍 Weather in {city_name}:")
        print(f"🌡 Temperature: {temperature}°C")
        print(f"🌬 Wind Speed: {wind_speed} km/h")
        print(f"☁ Condition Code: {condition} (Check API docs for description)")

    except Exception as e:
        print(f"❌ Error: {e}")

city_name = input("Enter city name: ")
get_weather(city_name)
