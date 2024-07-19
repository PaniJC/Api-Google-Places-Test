import requests


API_KEY = ""
RESTAURANT_NAME = "Ragatzi"

place_id = ["ChIJgUbEo8cfqokR5lP9_Wh_DaM", "GhIJQWDl0CIeQUARxks3icF8U8A", "EicxMyBNYXJrZXQgU3QsIFdpbG1pbmd0b24sIE5DIDI4NDAxLCBVU0E", "IhoSGAoUChIJ0U6OoscfqokR6P225pApu2UQDQ"]

def get_place_details(api_key, place_id):
    url = f"https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&key={api_key}"
    
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("API request failed")
    print(response.json())
    return response.json()


def search_restaurant_by_name(api_key, restaurant_name, location=None, radius=5000):
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {
        'query': restaurant_name,
        'key': api_key,
        'type': 'restaurant'
    }
    
    if location:
        params['location'] = location
        params['radius'] = radius
    
    response = requests.get(url, params=params)
    
    if response.status_code != 200:
        raise Exception(f"API request failed with status code {response.status_code}")
    
    #print(response.json())
    
    results = response.json().get('results', [])
    #print(results)
    
    return results


# get_place_details(API_KEY, place_id[2])
restaurants_results =  search_restaurant_by_name(API_KEY, RESTAURANT_NAME)

for restaurant in restaurants_results:
    opening_hours = restaurant.get('opening_hours', {})
    open_now = opening_hours.get('open_now', False)
    
    print(f"Nombre: {restaurant.get('name')}")
    print(f"Dirección: {restaurant.get('formatted_address')}")
    print(f"Estado del negocio: {restaurant.get('business_status')}")
    print(f"Abierto ahora?: {open_now}")
    print(f"Calificación: {restaurant.get('rating')}")
    print("---")
