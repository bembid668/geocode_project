import pandas as pd
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

input_filename = 'addresses.csv'
output_filename = 'output.csv'
final_filename = 'final.csv'

data = pd.read_csv(input_filename, encoding='utf8')
address_column_name = "Address"
addresses = data[address_column_name].tolist()
geolocator = Nominatim(user_agent="bambi_script")
output = {}

def get_geolocation(address):
    location = geolocator.geocode(address)
    output = {
        "address" : location.address,
        "coordinates" : (location.latitude, location.longitude)
    }
    return output

results = []

for address in addresses:
    geo_result = get_geolocation(address)
    final_output = {}
    results.append(geo_result)

df = pd.DataFrame(results)
final_distance = []
city_centre = (55.861170, -4.249562)

for index, row in df.iterrows():
    address = row['address']
    coordinates = row['coordinates']
    distance = geodesic(city_centre, coordinates)
    final_output = {'address' : address,
            'coordinates' : coordinates,
            'distance' : distance}
    final_distance.append(final_output)

print(final_distance)
# pd.DataFrame(final_distance).to_csv(final_filename, encoding='utf8')
