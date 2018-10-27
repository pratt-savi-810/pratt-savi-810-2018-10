#standard items: print, range
#different libraries part of standard python installation
#install your own python libraries (eg mp3 converter)
# datetime


import urllib
import datetime

todays_date = datetime.date.today()

url_list = [
    "https://data.cityofnewyork.us/api/geospatial/a9we-mtpn?method=export&format=Original",
    "https://data.cityofnewyork.us/api/views/varh-9tsp/rows.csv?accessType=DOWNLOAD"
]

filename_list = [
    "C:/Users/ksutton/Documents/Data/wifi_{0}_finalfinal.zip".format(todays_date),
    "C:/Users/ksutton/Documents/Data/wifi_{0}_for_excel.csv".format(todays_date)
]

for url_item, filename_item in zip(url_list, filename_list):
    print (url_item, filename_item)
    urllib.urlretrieve(url_item, filename_item)

