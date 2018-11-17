# import arcpy

import json
import urllib2
import pandas as pd

# Toronto Bikeshare json response url
bike_json_addr = 'https://tor.publicbikesystem.net/ube/gbfs/v1/'
# request = Request(bike_json_addr)

# receive json response
response = urllib2.urlopen(bike_json_addr)

# print(response)

# read raw response into python variable
bike_json = response.read()

# print(bike_json)

# load raw response as python dictionary
load_bike_json = json.loads(bike_json)

# print(load_bike_json)
# print(load_bike_json['data']['en']['feeds'][1])

# pull list of bikeshare json feed urls
feeds_bike_json = load_bike_json['data']['en']['feeds']

# print(feeds_bike_json[1]['name'])

# initialize station info deed url variable
station_info_url = ''

# loop through feeds to find station info url
for url_loop in feeds_bike_json:
    # print(url_loop)
    if url_loop['name'] == 'station_information':
        station_info_url = url_loop['url']

# print(station_info_url)

# raw_bike_pd = pd.read_json(bike_json, 'index')

# print(raw_bike_pd)

# url_bike_pd = pd.read_json(raw_bike_pd, 'values')

# print(url_bike_pd)

# receive json response
station_info_response = urllib2.urlopen(station_info_url)

# print(response)

# read raw response into python variable
station_info_json = station_info_response.read()

# print(bike_json)

# load raw response as python dictionary
load_station_info_json = json.loads(station_info_json)

# print(load_bike_json)
# print(load_bike_json['data']['en']['feeds'][1])

# pull list of data about bikeshare stations
station_list = load_station_info_json['data']['stations']

# print(station_list)

# loop through feeds to print station list
for station_loop in station_list:
    print(station_loop)
