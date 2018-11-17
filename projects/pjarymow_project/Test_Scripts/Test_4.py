import shutil
import os

gdb_path = r'J:\Pavlo\Pratt_XSAVI_810\Data'
shapefile_dir = r'J:\Pavlo\Pratt_XSAVI_810\Data\Shapefiles'


shutil.rmtree(gdb_path, ignore_errors=True)

os.mkdir(gdb_path)
os.mkdir(shapefile_dir)
