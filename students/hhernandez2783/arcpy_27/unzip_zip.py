import zipfile
import datetime

todays_date = datetime.date.today()

def unzip_file(zip_file_name, extract_location):
    zip_object = zipfile.ZipFile(zip_file_name, 'r')
    zip_object.extractall(extract_location)


unzip_file("C:\Users\hhernan9\Documents\GitHub\pratt-savi-810-2018-10\Students\Hector Hernandez\TEST\wifi_{0}final.zip".format(todays_date),
           "C:\Users\hhernan9\Documents\GitHub\pratt-savi-810-2018-10\Students\Hector Hernandez\TEST\ new folder{0}".format(todays_date))