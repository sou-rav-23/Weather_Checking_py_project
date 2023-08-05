
# #⚡##  first install request module by below command :  
# # python -m pip install requests

import requests

# # city_name = str(input("𝙀𝙣𝙩𝙚𝙧 𝙔𝙤𝙪𝙧 𝘾𝙞𝙩𝙮 𝙉𝙖𝙢𝙚 : "))
city_name = input("Enter Your City Name: ")

api_key = "d0134831064a714061e10883ebaee506"
# # api_key = str(input("enter_your_openWeather_api-key : "))

def get_weather(api_key, city_name):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"

    try:
        response = requests.get(url).json()  # sending get request and storing the data in json format(object) from server through api
        # print(response)
        temperature = response["main"]["temp"]

        Temp = temperature - 273.15        # convert to C
        celsius = format(Temp,".2f")    #format to show only first 2 numbers after the dot  example 23.12210000 = 23.12

        # celsius = "{:.2f}".format(temperature - 273.15)      # convert  to C
        # celsius = "{:.2f}".format(temperature/10)      # show temperature in floating data type

        # # celsius = math.ceil(temperature/10)          # show temperature in integer data type
        print("The temperature in", city_name, "is", str(celsius) + "°C")
    except :
        print("Error: Invalid city name or Data fetching failed.")


get_weather(api_key, city_name)