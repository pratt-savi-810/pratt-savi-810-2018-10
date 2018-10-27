import zipfile
import datetime

todays_date = datetime.date.today()

def unzip_file(zip_file_name, extract_location):
    zip_object = zipfile.ZipFile(zip_file_name, 'r')
    zip_object.extractall(extract_location)

unzip_file(
        "C:/Users/ksutton/Documents/Data/wifi_{0}_finalfinal.zip".format(todays_date),
        "C:/Users/ksutton/Documents/Data/wifi/MYFOLDER"#.format(todays_date)
)