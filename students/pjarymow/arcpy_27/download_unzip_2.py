import urllib
import datetime

# print datetime.date.today()

todays_date = datetime.date.today()

url_list = [
    # "https://data.cityofnewyork.us/api/geospatial/a9we-mtpn?method=export&format=Shapefile",
    "https://data.cityofnewyork.us/api/geospatial/a9we-mtpn?method=export&format=Original",
    "https://data.cityofnewyork.us/api/views/varh-9tsp/rows.csv?accessType=DOWNLOAD"
]

filename_list = [
    "C:/Users/pjarymow/Documents/GitHub/pratt-savi-810-2018-10/students/pjarymow/arcpy_27/data-10_27_2018/wifi_{0}_final.zip".format(todays_date),
    "C:/Users/pjarymow/Documents/GitHub/pratt-savi-810-2018-10/students/pjarymow/arcpy_27/data-10_27_2018/wifi_{0}_for_excel_final.csv".format(todays_date)
]

for url_item, filename_item in zip(url_list, filename_list):
    print(url_item, filename_item)
    urllib.urlretrieve(url_item, filename_item)

#for url_item in url_list:
#    print(url_item)
#    urllib.urlretrieve(
#        url_item,
#        "C:/Users/pjarymow/Documents/GitHub/pratt-savi-810-2018-10/students/pjarymow/arcpy_27/data2_{0}_{1}".format(
#            url_item.split('=')[1],
#            todays_date)
#    )

