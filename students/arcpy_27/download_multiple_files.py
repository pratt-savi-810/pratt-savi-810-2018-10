import urllib
import datetime

todays_date = datetime.date.today()

url_list = ["https://data.cityofnewyork.us/api/geospatial/a9we-mtpn?method=export&format=Shapefile",
            "https://data.cityofnewyork.us/api/views/varh-9tsp/rows.csv?accessType=DOWNLOAD"]

filename_list = ["C:/Users/cwunsch/Documents/data/wifi_{0} finalfinal.zip".format(todays_date),
                 "C:/Users/cwunsch/Documents/data/wifi_{0} for excel.csv".format(todays_date)
                 ]

for url_item, filename_item, in zip(url_list, filename_list): #you need the zip() to run through a lists

    print (url_item, filename_item)

    urllib.urlretrieve(url_item, filename_item)
