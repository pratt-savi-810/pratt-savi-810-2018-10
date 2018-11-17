import Functions
import arcpy
import pandas as pd
import urllib
import zipfile

bike_json_addr = 'https://tor.publicbikesystem.net/ube/gbfs/v1/'
csv_dir = r'J:/Pavlo/Pratt_XSAVI_810/Data/station_list.csv'

gdb_dir = r'J:/Pavlo/Pratt_XSAVI_810/Data'
gdb_name = r'Test_GDB'
gdb_path = gdb_dir + r'/' + gdb_name + r'.gdb'
feature_dataset_name = 'Bikeshare'

# print(gdb_path)

shapefile_dir = r'J:/Pavlo/Pratt_XSAVI_810/Data/Shapefiles'

bikelane_data_url = 'http://opendata.toronto.ca/gcc/bikeways_mtm3.zip'
bikelane_data_zip_path = r'J:/Pavlo/Pratt_XSAVI_810/Data/Shapefiles/mtm3.zip'

Functions.clear_data_dir(gdb_dir, shapefile_dir)

station_list = Functions.get_station_list(bike_json_addr)
Functions.station_list_to_csv(station_list, csv_dir)

arcpy.CreateFileGDB_management(gdb_dir, gdb_name, "CURRENT")

urllib.urlretrieve(bikelane_data_url, bikelane_data_zip_path)

zip_ref = zipfile.ZipFile(bikelane_data_zip_path, 'r')
zip_ref.extractall(shapefile_dir)
zip_ref.close()

arcpy.CreateFeatureDataset_management(gdb_path, feature_dataset_name)

arcpy.FeatureClassToGeodatabase_conversion(Input_Features="J:/Pavlo/Pratt_XSAVI_810/Data/Shapefiles/CENTRELINE_BIKEWAY_OD.shp",
                                           Output_Geodatabase="J:/Pavlo/Pratt_XSAVI_810/Data/Test_GDB.gdb/Bikeshare")
