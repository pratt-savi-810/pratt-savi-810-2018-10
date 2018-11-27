import googlemaps
import pandas as pd

gmaps = googlemaps.Client(key='AIzaSyBZfnMGp21bQJznnjFubSQ0HNHR7RzX9gg')

# read file
df = pd.read_csv('cartel2.csv', delimiter=';')


# function that returns the coordinates given an address
def get_geolocation(address):

    response = gmaps.geocode(address)
    coordinates = response[0]['geometry']['location']
    return [coordinates['lat'], coordinates['lng']]


# Geocoding all rows!
df['coordinates'] = df['address'].apply(get_geolocation)
df[['lat','lon']] = pd.DataFrame(df.coordinates.values.tolist(), index= df.index)

# write file
df.to_csv('geocodedxx.csv', index=False)