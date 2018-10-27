# import datetime

# print(f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S}")

# print(datetime.datetime.now())

## # ##

# import arcpy
## from arcpy import geoprocessing

import urllib
#urllib.urlretrieve(
#    'https://data.cityofnewyork.us/api/geospatial/a9we-mtpn?method=export&format=Shapefile',
#    'C:/Users/dcook13/Documents/data/wifi.zip'
#)

x = 'dog'
y = 'frenchie'
print('the best {0} is {1}').format(x,y)

import datetime
todays_date = datetime.date.today()

urllib.urlretrieve(
    'https://data.cityofnewyork.us/api/geospatial/a9we-mtpn?method=export&format=Shapefile',
    'C:/Users/dcook13/Documents/data/wifi_{0}.zip'.format(todays_date)
    # same as /wifi' + todays_date + '.zip'
)

url_list = [
    'https://data.cityofnewyork.us/api/geospatial/a9we-mtpn?method=export&format=Original',
    'https://data.cityofnewyork.us/api/views/varh-9tsp/rows.csv?accessType=DOWNLOAD',
]

filename_list = [
    'C:/Users/dcook13/Documents/data/wifi_{0}_orig.zip'.format(todays_date),
    'C:/Users/dcook13/Documents/data/wifi_{0}_for_excel.csv'.format(todays_date),
]

for url_item, filename_item in zip(url_list, filename_list):
    print(url_item, filename_item)
    urllib.urlretrieve(url_item,filename_item)


















