import zipfile
import datetime
import arcpy

shape_folder = 'C:/Users/jbagtas/Documents/Data/MYFOLDER2018-10-27'  #folder name where shp file is
input_points = 'geo_export_a5a4a32b-ae98-4bbb-a131-8c86d5f82bd6' #file name of shp file

#the following was taken from Copy as Python Snippet in ArcCatalog and you can edit eg, add _v2 to file name
arcpy.Buffer_analysis("C:/Users/jbagtas/Documents/Data/MYFOLDER2018-10-27/geo_export_a5a4a32b-ae98-4bbb-a131-8c86d5f82bd6.shp",
                      "C:/Users/jbagtas/Documents/Data/MYFOLDER2018-10-27/geo_export_a5a4a32bae984bbba__buff_dissolv.shp",
                      "100 Feet",
                      dissolve_option = 'ALL' #according to Help docs this needs to be string
                      #can remove some of the other things like in_feature b4 "C:/Users" etc
                      #myFunction(param_1='pizza',param_2='beer') is the same as myFunction('pizza', 'beer') as long as it's in order
                      #the parameters need to be specified if you're not going in exact order (like skipping from param 3 to param5
                      #these are the minimum paramters needed
                      #other parameters exist but  the defaults were applied bc they weren't specified
)



