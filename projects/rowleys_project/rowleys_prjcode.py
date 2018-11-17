##extractzipfile
#importzipfile
#
#zip_folder='D:\PythonforArcGIS\ClassProject\ACS_16_5YR_B25070.zip'
#destination='D:\PythonforArcGIS\ClassProject\data'
#
#zip_ref=zipfile.ZipFile(zip_folder,'r')
#zip_ref.extractall(destination)
#zip_ref.close()

#changefieldnames
import arcpy
import pandas as pd

file = r'D:\PythonforArcGIS\ClassProject\Data\ACS_16_5YR_B25070.csv'
rent_df = pd.read_csv(file)



# rent.rename(columns={'GEO.id':'GEOid','GEO.id2':'GEOid2','GEO.display-label':'Geography'}inplace=True)
# r?

##makecolumnofdataframestring
#rent.head()
#rent['geoid2']=rent.geoid2.astype(string)

#Joindataframes



