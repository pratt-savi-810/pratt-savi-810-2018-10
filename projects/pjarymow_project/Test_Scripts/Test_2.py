import Functions
import arcpy
import pandas as pd

bike_json_addr = 'https://tor.publicbikesystem.net/ube/gbfs/v1/'
csv_dir = r'J:\Pavlo\Pratt_XSAVI_810\Data\station_list.csv'

station_list = Functions.get_station_list(bike_json_addr)

# print(station_list[0]['lon'])

# for station in station_list:
#     print(station['lon'])

# station_list_latlong['lat'] = station_list['lat']

station_list_df = pd.DataFrame(station_list)

station_list_df.to_csv(csv_dir, encoding='utf-8')

print(station_list_df)
