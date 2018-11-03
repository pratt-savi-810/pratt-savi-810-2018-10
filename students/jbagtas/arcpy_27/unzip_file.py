import zipfile
import datetime

todays_date = datetime.date.today()

def unzip_file(zip_file_name, extract_location):
   zip_object =  zipfile.ZipFile(zip_file_name, 'r')
   zip_object.extractall(extract_location)


unzip_file(
    "C:/Users/jbagtas/Documents/Data/wifi_{0}.zip".format(todays_date), #make sure this matches the file you DL'd since you're not redownloading
    "C:/Users/jbagtas/Documents/Data/MYFOLDER{0}".format(todays_date) #creating a new folder here
)

