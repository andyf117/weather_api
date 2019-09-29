# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests
import time
import json
# Import API key
from api_keys import api_key

# Incorporated citipy to determine city based on latitude and longitude
from citipy import citipy

# Output File (CSV)
output_data_file = "output_data/cities.csv"

# Range of latitudes and longitudes
lat_range = (-90, 90)
lng_range = (-180, 180)


# List for holding lat_lngs and cities
lat_lngs = []
cities = []

# Create a set of random lat and lng combinations
lats = np.random.uniform(low=-90.000, high=90.000, size=1500)
lngs = np.random.uniform(low=-180.000, high=180.000, size=1500)
lat_lngs = zip(lats, lngs)

# Identify nearest city for each lat, lng combination



for lat_lng in lat_lngs:

    city = citipy.nearest_city(lat_lng[0], lat_lng[1]).city_name
    
    # If the city is unique, then add it to a our cities list
    if city not in cities:
        cities.append(city)

# Print the city count to confirm sufficient count
print(len(cities))

dataframe_ = pd.DataFrame(columns=['City', 'Country', 'Date', 'Humidity', 'Lat', 'Long', 'Max Temp', 'Wind Speed'])


for city in cities:
    
    url = 'https://samples.openweathermap.org/data/2.5/weather?q=' + str(city) + '&appid=b6907d289e10d714a6e88b30761fae22'
    print(url)
    response = requests.get(url)
    print(response)
    json_data = json.loads(response.text)

    city = city
    cloudiness = json_data['clouds']
    country = json_data['name']
    date = json_data['dt']
    humidity = json_data['main']
    humidity = humidity['humidity']
    
    coord = json_data['coord']
    lat = coord['lat']
    lon = coord['lon']
    
    temp = json_data['main']
    temp = temp['temp_max']
    
    wind = json_data['wind']
    wind = wind['speed']

    dictionary = {
    'City':city, 
    'Cloudiness':cloudiness, 
    'Country':country, 
    'Date':date, 
    'Humidity': humidity, 
    'Lat': lat, 
    'Long': lon, 
    'Max Temp': temp, 
    'Wind Speed': wind,


    }

    dataframe_.append(dictionary, ignore_index=True)

print(dataframe_)

dataframe_.to_csv('dfnew.csv')

lattitude = dataframe_['Lat'].tolist()
maxtemperaature = dataframe_['Max Temp'].tolist()
cloudiness = dataframe_['Cloudiness'].tolist()
windspeed = dataframe_['Wind Speed'].tolist()

plt.scatter(lattitude,maxtemperaature)
plt.show()

plt.scatter(lattitude,humidity)
plt.show()

plt.scatter(lattitude,cloudiness)
plt.show()

plt.scatter(lattitude,windspeed)
plt.show()


