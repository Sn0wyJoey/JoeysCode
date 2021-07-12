import colors as c
import requests

Space = (" >")
print("Welcome to the Weather Program!")
while True:
    try:
        City = input("What city do you want?" + Space).strip()
        print(City)
        Url = f"http://api.openweathermap.org/data/2.5/weather?q={City}&appid=9983943652d2d1b8d93469627710b91d&units=imperial"
        weather = requests.get(Url).json()
        Temp = weather["main"]["temp"] 
        Humidity = weather["main"]["humidity"]
        Forecast = weather["weather"][0]["main"]
        print("The Temperature Is" , Temp , "F")
        print("The Humidity Is" , Humidity , "%")
        print("The Forecast is " + Forecast)
    except KeyError:
        print("That is not a city")
    yes = input("Do you want to look up another city?" + Space).lower()
    if yes in ["yes" , "yea" , "ok" , "sure"]:
        pass
    else:
        break
print("Thank You for using the Weather Program!")
exit()