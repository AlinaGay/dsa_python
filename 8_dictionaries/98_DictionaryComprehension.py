import random

# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key,value) in dict.items()}
# new_dict = {new_key:new_value for (key,value) in dict.items() if condition}

city_names = ['Paris','Madrid','London','Berlin','Roma']

city_temps = {city: random.randint(20,30) for city in city_names}
print(city_temps)

above_25 = {city: temp for (city,temp) in city_temps.items() if temp > 25}
print(above_25)