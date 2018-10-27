import zipfile
import datetime

todays_date = datetime.date.today()

def unzip_file(zip_file_name, extract_location):
    zip_object = zipfile.ZipFile(zip_file_name, 'r')
    zip_object.extractall(extract_location)


unzip_file(
    "C:/Users/pjarymow/Documents/GitHub/pratt-savi-810-2018-10/students/pjarymow/arcpy_27/data-10_27_2018/wifi_{0}_final.zip".format(todays_date),
    "C:/Users/pjarymow/Documents/GitHub/pratt-savi-810-2018-10/students/pjarymow/arcpy_27/data-10_27_2018/Unzipped_{0}".format(todays_date)
)

