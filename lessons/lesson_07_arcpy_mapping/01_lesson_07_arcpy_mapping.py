
import urllib

### THIS REQUIRES USING MACHINE WITH ARCGIS INSTALLED!!!!!!!!

url = 'http://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nybb_17c.zip'
your_zip_path = "data/nybb_17c.zip"

YOUR_WINDOWS_MACHINE_your_zip_path = "C:/Users/......."

urllib.urlretrieve(url, your_zip_path)

import zipfile

zip = zipfile.ZipFile(your_zip_path, 'r')
zip.extractall('data/')

### THIS REQUIRES USING MACHINE WITH ARCGIS INSTALLED!!!!!!!!

import arcpy

mxd = arcpy.mapping.MapDocument("CURRENT")
for pageNum in range(1, mxd.dataDrivenPages.pageCount + 1):
  mxd.dataDrivenPages.currentPageID = pageNum
  arcpy.mapping.ExportToPNG(mxd, "Y:/GitHub/pratt-savi-810-2017-10/img/" + str(pageNum) + ".png")
del mxd


mxd = arcpy.mapping.MapDocument("Y:/GitHub/pratt-savi-810-2017-10/data/nybb_map.mxd")
#can do it here ^

for pageNum in range(1, mxd.dataDrivenPages.pageCount + 1):
  mxd.dataDrivenPages.currentPageID = pageNum
  arcpy.mapping.ExportToPNG(mxd, "Y:/GitHub/pratt-savi-810-2017-10/img/" + str(pageNum) + "_arccatalog_ran.png")
del mxd
