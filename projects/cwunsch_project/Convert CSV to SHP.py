import pandas as pd
import arcpy

d1 = pd.read_csv(r'E:/GIS/Python/Python/Data REV/Lab_data_JOINED_AGOL/Wells_Lab_Join.csv')

arcpy.MakeXYEventLayer_management(
    r'E:/GIS/Python/Python/Data REV/Lab_data_JOINED_AGOL/Wells_Lab_Join.csv',
    'X',
    'Y',
    'XY_plot'
)

arcpy.CopyFeatures_management(
    'XY_plot',
    r'E:/GIS/Python/Python/Data REV/Well_w_LabData/Well_w_LabData.shp'
)