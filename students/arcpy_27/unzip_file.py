import zipfile
import datetime

todays_date = datetime.date.today()

def unzip_file(zip_file_name, extract_location):
    zip_object = zipfile.ZipFile(zip_file_name, 'r')
    zip_object.extractall(extract_location)

unzip_file(
    "C:/Users/cwunsch/Documents/data/wifi_{0} finalfinal.zip".format(todays_date),
    "C:/Users/cwunsch/Documents/data/wifi_MYFOLDER{0}".format(todays_date), #the {0} is the datetime place holder
)