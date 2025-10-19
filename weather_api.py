import requests

def get_weather(city, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=f6de65b2eafbeea1f71b99a130a3f161"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            print(f"\n Weather Report for {data['name']}, {data['sys']['country']}")
            print("-" * 40)
            print(f"Temperature: {data['main']['temp']}°C")
            print(f"Feels Like: {data['main']['feels_like']}°C")
            print(f"Weather: {data['weather'][0]['description'].capitalize()}")
            print(f"Humidity: {data['main']['humidity']}%")
            print(f"Wind Speed: {data['wind']['speed']} m/s")
            print("-" * 40)
        else:
            print("\n Error:", data.get("message", "Unable to fetch weather data."))

    except requests.exceptions.RequestException as e:
        print("\n Network Error:", e)

def main():
    print("=" * 40)
    print("       Simple Weather App (CLI) ")
    print("=" * 40)

    api_key = "f6de65b2eafbeea1f71b99a130a3f161"  

    while True:
        city = input("\nEnter city name (or 'exit' to quit): ").strip()
        if city.lower() == "exit":
            print("\n Exiting Weather App. Stay safe!")
            break
        elif city:
            get_weather(city, api_key)
        else:
            print("Please enter a valid city name.")

if __name__ == "__main__":
    main()
