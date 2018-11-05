#!/usr/bin/env python3
# Create a class to hold a city location. Call the class "City". It should have
# fields for name, latitude, and longitude.

# TODO
class City:
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# Use Python's built-in "csv" module to read this file so that each record is
# imported into a City instance. (You're free to add more attributes to the City
# class if you wish, but this is not necessary.) Google "python 3 csv" for
# references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.

from os import path
import csv
cities = []

csvpath = path.join(path.dirname(__file__), "cities.csv")
with open(csvpath, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        try:
            city = City(row["city"], float(row["lat"]), float(row["lng"]))
            cities.append(city)
        except ValueError:
            # just skip cities that we can't deserialize
            pass

# Print the list of cities (name, lat, lon), 1 record per line.

for city in cities:
    print(city.name, city.latitude, city.longitude)
