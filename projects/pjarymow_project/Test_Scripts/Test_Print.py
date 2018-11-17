import Functions

bike_json_addr = 'https://tor.publicbikesystem.net/ube/gbfs/v1/'
csv_dir = r'J:\Pavlo\Pratt_XSAVI_810\Data\station_list.csv'

print(Functions.get_station_list(bike_json_addr))

station_list = Functions.get_station_list(bike_json_addr)

for station_loop in station_list:
    print(station_loop)

Functions.station_list_to_csv(station_list, csv_dir)
