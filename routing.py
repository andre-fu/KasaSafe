import requests
import googlemaps
from datetime import datetime
from json.decoder import JSONDecodeError
import json
from random import *

class routing:
    def __init__(self):
        self.lat = 0
        self.lat = 0
        self.possible = []

        response = requests.post(url="https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyD8np92Z7kxjUMm9jSFE2Y97SzB0QCToUE")

        for key in response.json():
            if key == "location":
                for key2 in response.json()[key]:
                    if key2 == "lat":
                        self.lat = response.json()[key][key2]
                    if key2 == "lng":
                        self.long = response.json()[key][key2]
        self.loc = (self.lat, self.long)

    def possible_places(self):
        response = requests.get(
            "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=" + str(self.lat) +","+ str(self.long) +"&type=cafe&radius=500&key=AIzaSyD8np92Z7kxjUMm9jSFE2Y97SzB0QCToUE")
        # print(response.status_code)
        # print("")
        # print("")
        cafe = response.json()
        # print(json.dumps(response.json(), sort_keys=True, indent=4))

        for key1 in cafe:
            if key1 == "results":
                # print(key1)
                for item in cafe[key1]:
                    # print(isinstance(item, dict))
                    for key in item:
                        if key == "name":
                            self.possible.append(item[key])

        response = requests.get(
            "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=" + str(self.lat) +","+ str(self.long) +"&type=restaurant&radius=500&key=AIzaSyD8np92Z7kxjUMm9jSFE2Y97SzB0QCToUE")
        # print(response.status_code)
        # print("")
        # print("")
        restaurants = response.json()
        # print(json.dumps(response.json(), sort_keys=True, indent=4))

        for key1 in restaurants:
            if key1 == "results":
                # print(key1)
                for item in restaurants[key1]:
                    # print(isinstance(item, dict))
                    for key in item:
                        if key == "name":
                            self.possible.append(item[key])

        response = requests.get(
            "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=" + str(self.lat) +","+ str(self.long) +"&type=bakery&radius=500&key=AIzaSyD8np92Z7kxjUMm9jSFE2Y97SzB0QCToUE")
        # print(response.status_code)
        # print("")
        # print("")
        bakery = response.json()
        # print(json.dumps(response.json(), sort_keys=True, indent=4))

        for key1 in bakery:
            if key1 == "results":
                # print(key1)
                for item in bakery[key1]:
                    # print(isinstance(item, dict))
                    for key in item:
                        if key == "name":
                            self.possible.append(item[key])

        response = requests.get(
            "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=" + str(self.lat) +","+ str(self.long) +"&type=bar&radius=500&key=AIzaSyD8np92Z7kxjUMm9jSFE2Y97SzB0QCToUE")
        # print(response.status_code)
        # print("")
        # print("")
        bar = response.json()
        # print(json.dumps(response.json(), sort_keys=True, indent=4))

        for key1 in bar:
            if key1 == "results":
                # print(key1)
                for item in bar[key1]:
                    # print(isinstance(item, dict))
                    for key in item:
                        if key == "name":
                            self.possible.append(item[key])

        response = requests.get(
            "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=" + str(self.lat) +","+ str(self.long) +"&type=parking&radius=500&key=AIzaSyD8np92Z7kxjUMm9jSFE2Y97SzB0QCToUE")
        # print(response.status_code)
        # print("")
        # print("")
        parking = response.json()
        # print(json.dumps(response.json(), sort_keys=True, indent=4))

        for key1 in parking:
            if key1 == "results":
                # print(key1)
                for item in parking[key1]:
                    # print(isinstance(item, dict))
                    for key in item:
                        if key == "name":
                            self.possible.append(item[key])

        response = requests.get(
            "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=" + str(self.lat) +","+ str(self.long) +"&type=taxi_stand&radius=500&key=AIzaSyD8np92Z7kxjUMm9jSFE2Y97SzB0QCToUE")
        # print(response.status_code)
        # print("")
        # print("")
        taxi_stand = response.json()
        # print(json.dumps(response.json(), sort_keys=True, indent=4))

        for key1 in taxi_stand:
            if key1 == "results":
                # print(key1)
                for item in taxi_stand[key1]:
                    # print(isinstance(item, dict))
                    for key in item:
                        if key == "name":
                            self.possible.append(item[key])

        response = requests.get(
            "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=" + str(self.lat) +","+ str(self.long) +"&type=gas_station&radius=1000&key=AIzaSyD8np92Z7kxjUMm9jSFE2Y97SzB0QCToUE")
        # print(response.status_code)
        # print("")
        # print("")
        gas_station = response.json()
        # print(json.dumps(response.json(), sort_keys=True, indent=4))

        for key1 in gas_station:
            if key1 == "results":
                # print(key1)
                for item in gas_station[key1]:
                    # print(isinstance(item, dict))
                    for key in item:
                        if key == "name":
                            self.possible.append(item[key])

        response = requests.get(
            "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=" + str(self.lat) +","+ str(self.long) +"&type=rv_park&radius=1000&key=AIzaSyD8np92Z7kxjUMm9jSFE2Y97SzB0QCToUE")
        # print(response.status_code)
        # print("")
        # print("")
        rv_park = response.json()
        # print(json.dumps(response.json(), sort_keys=True, indent=4))

        for key1 in rv_park:
            if key1 == "results":
                # print(key1)
                for item in rv_park[key1]:
                    # print(isinstance(item, dict))
                    for key in item:
                        if key == "name":
                            self.possible.append(item[key])

        response = requests.get(
            "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=" + str(self.lat) +","+ str(self.long) +"&type=lodging&radius=1000&key=AIzaSyD8np92Z7kxjUMm9jSFE2Y97SzB0QCToUE")
        # print(response.status_code)
        # print("")
        # print("")
        lodging = response.json()
        # print(json.dumps(response.json(), sort_keys=True, indent=4))

        for key1 in lodging:
            if key1 == "results":
                # print(key1)
                for item in lodging[key1]:
                    # print(isinstance(item, dict))
                    for key in item:
                        if key == "name":
                            self.possible.append(item[key])

        response = requests.get(
            "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=" + str(self.lat) +","+ str(self.long) +"&type=mosque&radius=1000&key=AIzaSyD8np92Z7kxjUMm9jSFE2Y97SzB0QCToUE")
        # print(response.status_code)
        # print("")
        # print("")
        mosque = response.json()
        # print(json.dumps(response.json(), sort_keys=True, indent=4))

        for key1 in mosque:
            if key1 == "results":
                # print(key1)
                for item in mosque[key1]:
                    # print(isinstance(item, dict))
                    for key in item:
                        if key == "name":
                            self.possible.append(item[key])

        response = requests.get(
            "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=" + str(self.lat) +","+ str(self.long) +"&type=hindu_temple&radius=1000&key=AIzaSyD8np92Z7kxjUMm9jSFE2Y97SzB0QCToUE")
        # print(response.status_code)
        # print("")
        # print("")
        hindu_temple = response.json()
        # print(json.dumps(response.json(), sort_keys=True, indent=4))

        for key1 in hindu_temple:
            if key1 == "results":
                # print(key1)
                for item in hindu_temple[key1]:
                    # print(isinstance(item, dict))
                    for key in item:
                        if key == "name":
                            self.possible.append(item[key])

        response = requests.get(
            "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=" + str(self.lat) +","+ str(self.long) +"&type=church&radius=1000&key=AIzaSyD8np92Z7kxjUMm9jSFE2Y97SzB0QCToUE")
        # print(response.status_code)
        # print("")
        # print("")
        church = response.json()
        # print(json.dumps(response.json(), sort_keys=True, indent=4))

        for key1 in church:
            if key1 == "results":
                # print(key1)
                for item in church[key1]:
                    # print(isinstance(item, dict))
                    for key in item:
                        if key == "name":
                            self.possible.append(item[key])

    def chooser(self):
        ra_idx = randint(0, len(self.possible))

        return self.possible[ra_idx]
        

    def routes(self, origin, destination):
        gmaps = googlemaps.Client(key='AIzaSyD8np92Z7kxjUMm9jSFE2Y97SzB0QCToUE')

        # Geocoding an address
        geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

        # Look up an address with reverse geocoding
        reverse_geocode_result = gmaps.reverse_geocode((self.lat, self.long))

        # Request directions via public transit
        now = datetime.now()
        directions_result = gmaps.directions(origin,
                                            destination,
                                            mode="driving",
                                            departure_time=now)

        # print(json.dumps(directions_result, sort_keys=True, indent=4))

        for item in directions_result:
            for key in item:
                if key == "legs":
                    for item1 in item[key]:
                        for key2 in item1:
                            if key2 == "steps":
                                for item2 in item1[key2]:
                                    for key3 in item2:
                                        if key3 == "html_instructions":
                                            print(item2[key3])
    
""" if __name__ == "__main__":
    #test = routing()
    #test.possible_places()
    #type(test.possible_places())
    #start = "1426 Bishop Street, Montreal, Canada"
    #end = "Bahen Center for Information Technology, Toronto, Canada"
    print("--------------------------------------------------1----------------------------------------------------------")
    print("------------------------------------------------------------------------------------------------------------")
    #test.routes(start, end)

    route = routing()
    places = route.possible_places()
    choice = route.chooser()
    print(choice)
    start = route.loc
    print(route.loc)
    end = choice
    print("---------------------------------------------------2---------------------------------------------------------")
    print("------------------------------------------------------------------------------------------------------------")
    instructions = route.routes(start, end) """














