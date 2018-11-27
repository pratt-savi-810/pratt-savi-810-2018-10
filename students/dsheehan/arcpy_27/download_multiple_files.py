import urllib
import datetime
import time


todays_date = datetime.date.today()

url_list = [
    "https://data.cityofnewyork.us/api/geospatial/a9we-mtpn?method=export&format=Original",
    "https://data.cityofnewyork.us/api/views/varh-9tsp/rows.csv?accessType=DOWNLOAD",
]

filename_list = [
    "C:/Users/Riches/Documents/GitHub/pratt-savi-810-2018-10/projects/RICHES PROJECT.zip".format(todays_date),
    "C:/Users/Riches/Documents/GitHub/pratt-savi-810-2018-10/projects/RICHES PROJECT.csv".format(todays_date)
]

for url_item, filename_item in zip(url_list, filename_list):

    print(url_item, filename_item)

    urllib.urlretrieve(url_item, filename_item)

    time.sleep(20)




dnknkn