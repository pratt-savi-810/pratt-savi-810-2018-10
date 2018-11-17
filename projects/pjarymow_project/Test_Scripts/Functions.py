import arcpy
import json
import urllib
import urllib2
import pandas as pd
import shutil
import os


def get_station_list(bike_json_addr):
    # bike_json_addr = Toronto Bikeshare json response url

    # receive json response
    response = urllib2.urlopen(bike_json_addr)

    # read raw response into python variable
    bike_json = response.read()

    # load raw response as python dictionary
    load_bike_json = json.loads(bike_json)

    # pull list of bikeshare json feed urls
    feeds_bike_json = load_bike_json['data']['en']['feeds']

    # initialize station info deed url variable
    station_info_url = ''

    # loop through feeds to find station info url
    for url_loop in feeds_bike_json:
        if url_loop['name'] == 'station_information':
            station_info_url = url_loop['url']

    # receive json response
    station_info_response = urllib2.urlopen(station_info_url)

    # read raw response into python variable
    station_info_json = station_info_response.read()

    # load raw response as python dictionary
    load_station_info_json = json.loads(station_info_json)

    # pull list of data about bikeshare stations
    station_list = load_station_info_json['data']['stations']

    return station_list


def station_list_to_csv(station_list, csv_dir):
    station_list_df = pd.DataFrame(station_list)
    station_list_df.to_csv(csv_dir, encoding='utf-8')


def clear_data_dir(gdb_path, shapefile_dir):
    # delete data directory
    shutil.rmtree(gdb_path, ignore_errors=True)

    # create empty directories for geodatabase and shapefiles
    os.mkdir(gdb_path)
    os.mkdir(shapefile_dir)
