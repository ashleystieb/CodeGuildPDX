import requests, random

PLACES_API_KEY = 'AIzaSyDZgZP1nCzUht2Ap-0Jy8ciBE50EI-NzmA'
GEO_CODE_API_KEY = 'AIzaSyBrLo3h5JLrTxb0DE-bHL6V2j7A1NYWURU'


def geo_code_location(city, state, sensor=False):
    global GEO_CODE_API_KEY
    base_url = 'https://maps.googleapis.com/maps/api'
    geocode_api_url = base_url + '/geocode/json?address={},+{}&key={}'.format(city, state, GEO_CODE_API_KEY)
    geo_coded_location = requests.get(geocode_api_url).json()
    coordinates = geo_coded_location['results'][0]['geometry']['location']
    return coordinates['lat'], coordinates['lng']


def get_places_high(city, state, keyword, type='restaurant', radius=50000):
    global PLACES_API_KEY
    base_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='
    coordinate_tuple = geo_code_location(city, state)
    lat, lng = coordinate_tuple[0], coordinate_tuple[1]
    places_high = base_url + "{},{}&type={}&keyword={}+food&radius={}&minprice=4&maxprice=4&opennow&key={}".format(lat, lng, type, keyword, radius, PLACES_API_KEY)
    nearby_places = requests.get(places_high).json()
    restaurant_list = []
    for place in nearby_places['results']:
        if place['name'] not in restaurant_list:
            restaurant_list.append(place['name'])
    print(restaurant_list)
    return random.choice(restaurant_list)


def get_places_low(city, state, keyword, type='restaurant', radius=50000):
    global PLACES_API_KEY
    base_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='
    coordinate_tuple = geo_code_location(city, state)
    lat, lng = coordinate_tuple[0], coordinate_tuple[1]
    places_low = base_url + "{},{}&type={}&keyword={}+food&radius={}&minprice=0&maxprice=1&opennow&key={}".format(lat, lng, type, keyword, radius, PLACES_API_KEY)
    nearby_places = requests.get(places_low).json()
    restaurant_list = []
    for place in nearby_places['results']:
        if place['name'] not in restaurant_list:
            restaurant_list.append(place['name'])
    print(restaurant_list)
    return random.choice(restaurant_list)


def get_places_med(city, state, keyword, type='restaurant', radius=50000):
    global PLACES_API_KEY
    base_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='
    coordinate_tuple = geo_code_location(city, state)
    lat, lng = coordinate_tuple[0], coordinate_tuple[1]
    places_med = base_url + "{},{}&type={}&keyword={}+food&radius={}&minprice=2&maxprice=3&opennow&key={}".format(lat, lng, type, keyword, radius, PLACES_API_KEY)
    nearby_places = requests.get(places_med).json()
    restaurant_list = []
    for place in nearby_places['results']:
        if place['name'] not in restaurant_list:
            restaurant_list.append(place['name'])
    print(restaurant_list)
    return random.choice(restaurant_list)


def main():
    city = input("Enter a city: ")
    state = input("Enter a state: ")
    keyword = input("Enter a type of food: ")
    price = input("Enter a price range ($, $$, $$$): ")
    if price == '$':
        results = get_places_low(city, state, keyword)
        print("You should eat at {}.".format(results))
    elif price == '$$':
        results = get_places_med(city, state, keyword)
        print("You should eat at {}.".format(results))
    elif price == '$$$':
        results = get_places_high(city, state, keyword)
        print("You should eat at {}.".format(results))
    else:
        print("Error.")


main()
