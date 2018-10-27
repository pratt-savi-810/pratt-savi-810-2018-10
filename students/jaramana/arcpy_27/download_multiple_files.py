import urllib
import datetime

todays_date = datetime.date.today()

url_list = [
    "https://data.cityofnewyork.us/api/views/rb9s-d3m8/rows.csv?accessType=DOWNLOAD",
]

filename_list = ["C:/Users/ashaiban/Documents/data/individual_landmarks.csv",
]

for url_item, filename_item in zip(url_list, filename_list):

    print(url_item,filename_item)

    urllib.urlretrieve(url_item, filename_item)
