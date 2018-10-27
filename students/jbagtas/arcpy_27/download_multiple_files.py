import datetime

print(datetime.datetime) # libary_name.object_or_tool_name
print(datetime.datetime.now()) # library_name.object_or_tool_name.attribute
# datetime.datetime bc just so happens library has same name as function eg
print(datetime.date.today())

import urllib

urllib.urlretrieve(
    "https://data.cityofnewyork.us/api/geospatial/a9we-mtpn?method=export&format=Shapefile",
    "C:\\Users\\jbagtas\Documents\\Data\\wifi.zip" #should be fwd slash
)
#be sure to put locations (url or file path) in double quotes

#to put the DL date at end for version control: APPEND

todays_date = datetime.date.today()

urllib.urlretrieve(
    "https://data.cityofnewyork.us/api/geospatial/a9we-mtpn?method=export&format=Shapefile",
    "C:\\Users\\jbagtas\Documents\\Data\\wifi" + str(todays_date) + '.zip'
)
#yields wifi2018-10-27.zip
# or

urllib.urlretrieve(
    "https://data.cityofnewyork.us/api/geospatial/a9we-mtpn?method=export&format=Shapefile",
    "C:\\Users\\jbagtas\Documents\\Data\\wifi_{0}.zip".format(todays_date)
) # {} points to an index. when you created todays_date it was put into an array with index  0
#yields wifi_2018-10-27.zip

#create a list with urls to DL
url_list = [
    "https://data.cityofnewyork.us/api/geospatial/a9we-mtpn?method=export&format=Shapefile",
    "https://data.cityofnewyork.us/api/views/varh-9tsp/rows.csv?accessType=DOWNLOAD"
]

#dcreate a list of filenames
filename_list = [
"C:\\Users\\jbagtas\Documents\\Data\\wifi_{0}.zip".format(todays_date),
"C:\\Users\\jbagtas\Documents\\Data\\wifi_{0}_for_excel.csv".format(todays_date)
]

for url_item, filename_item in zip(url_list, filename_list): #zip() helps w/iterations, just need it to iterate thru diff things
    print(url_item, filename_list) #to notify what urls it will retrieve in nxt line
    urllib.urlretrieve(url_item, filename_item)

