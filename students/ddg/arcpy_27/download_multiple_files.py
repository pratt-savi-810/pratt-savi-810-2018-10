import urllib
import datetime

todays_date = datetime.date.today()

url_list = [
    "https://data.cityofnewyork.us/api/geospatial/a9we-mtpn?method=export&format=Shapefile",
    "https://data.cityofnewyork.us/api/views/varh-9tsp/rows.csv?accessType=DOWNLOAD",
    "https://data.cityofnewyork.us/api/geospatial/a9we-mtpn?method=export&format=KML",
    "https://data.cityofnewyork.us/api/geospatial/tqmj-j8zm?method=export&format=Shapefile",
    "https://data.cityofnewyork.us/api/views/7t3b-ywvw/rows.csv?accessType=DOWNLOAD",
]

filename_list = [
    "C:/Users/dgoodma7/Documents/Data/wifi_{0}_final.zip".format(todays_date),
    "C:/Users/dgoodma7/Documents/Data/wifi_{0}_for_excel.csv".format(todays_date),
    "C:/Users/dgoodma7/Documents/Data/wifi_{0}_new.kml".format(todays_date),
    "C:/Users/dgoodma7/Documents/Data/wifi_{0}_boroughs.zip".format(todays_date),
    "C:/Users/dgoodma7/Documents/Data/wifi_{0}_boroughs_for_excel.csv".format(todays_date)

]

for url_item, filename_item in zip(url_list, filename_list):

    urllib.urlretrieve(url_item, filename_item)