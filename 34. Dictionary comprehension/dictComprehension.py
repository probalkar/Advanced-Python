# dictionary comprehension : a way to create a new dictionary with less syntax using an expression
#                            similar to list comprehension but with key-value pairs

# dictionary = {key: expression for (key,value) in dictionary.items()}
# dictionary = {key: expression for (key,value) in dictionary.items() if condition}
# dictionary = {key: expression if-else condition for (key,value) in dictionary.items()}
# dictionary = {key: function(value) for (key,value) in dictionary.items()}

# Example 1:
cities_in_F = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
cities_in_C = {key: round((value - 32) * (5/9)) for (key,value) in cities_in_F.items()}
print(cities_in_C)

# Example 2:
weather = {'New York': 'snowing', 'Boston': 'sunny', 'Los Angeles': 'sunny', 'Chicago': 'cloudy'}
sunny_weather = {key: value for (key,value) in weather.items() if value == 'sunny'}
print(sunny_weather)

# Example 3:
cities = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
desc_cities = {key: ("WARM" if value >= 50 else "COLD") for (key,value) in cities.items()}
print(desc_cities)

# Example 4:
def check_temp(value):
    if value >= 70:
        return "HOT"
    elif value >= 50 and value < 70:
        return "WARM"
    else:
        return "COLD"
    
cities = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
desc_cities = {key: check_temp(value) for (key,value) in cities.items()}
print(desc_cities)