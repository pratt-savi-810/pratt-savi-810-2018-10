
import urllib
import datetime

todays_date = datetime.date.today()

url_list = [

    "https://data.cityofnewyork.us/api/geospatial/a9we-mtpn?method=export&format=Shapefile",
    "https://data.cityofnewyork.us/api/views/varh-9tsp/rows.csv?accessType=DOWNLOAD"
    ]

filename_list = [
 'C:/Users/srowley4/Documents/pratt-savi-810-2018-10/Students/SheriRowley/data/wifi_{0}_final.zip'.format(todays_date),
 'C:/Users/srowley4/Documents/pratt-savi-810-2018-10/Students/SheriRowley/data/wifi_{0}_for_excel.csv'.format(todays_date)
 ]

for url_item, filename_item in zip(url_list, filename_list):
    print(url_item, filename_item)
    urllib.urlretrieve(url_item, filename_item)