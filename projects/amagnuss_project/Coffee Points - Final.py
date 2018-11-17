import arcpy
import pandas as pd
import json


arcpy.env.overwriteOutput = True


# Set the local variables
in_table = r'F:/GIS/Pratt/Ind. Study - Arc/CIAT Data/Coffee Points/CoffeePoints_2.csv'
List_of_Countries = ['Costa Rica', 'Guatemala', 'Mexico', 'Nicaragua', 'Honduras', 'El Salvador']

# Set dataframe, save separate new csvs for CAM countries
df = pd.read_csv(in_table, encoding='latin-1')

df_CAM = df[df['Country'].isin(List_of_Countries)]

for i in df_CAM['Country'].unique():
    dfc = df_CAM[df['Country'] == i]
    out_table = in_table.replace('.csv', '_{}.csv'.format(i))
    dfc.to_csv(out_table, index=False, encoding='utf-8')

print df_CAM.head(500)

# variables for xy plotting
for s in List_of_Countries:
    in_table_xy = r'F:\GIS\Pratt\Ind. Study - Arc\CIAT Data\Coffee Points\CoffeePoints_2_' + s + '.csv'
    out_feature_class = 'coffee_points'
    x_coords = "Longitude"
    y_coords = "Latitude"
    out_layer = 'coffeePoints' + s + '_CAM_lyr'
    saved_layer = r'F:/GIS/Pratt/Ind. Study - Arc/CIAT Data/Coffee Points/CoffeePoints_{}.csv'.format(s)

    # Set Arc workspace
    arcpy.env.workspace = r'F:/GIS/Pratt/Ind. Study - Arc/CoffeeData.gdb'


    arcpy.MakeXYEventLayer_management(
        in_table_xy,
        x_coords,
        y_coords,
        out_layer,
    )

    # reprojecting into NA Albers Equal Area

    # first shapefiles


     # Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script

    coffee_cfg = r'F:\GIS\Pratt\Ind. Study - Arc\CIAT Data\coffee_cfg.json'


    def read_config(config_json):
        with open(config_json) as f:
            data = json.load(f)
        return data


    d = read_config(coffee_cfg)

    print(
        d['data']['out_cs']
    )

    proj_filename = 'F:/GIS/Pratt/Ind. Study - Arc/CIAT Data/Coffee Points/AEA Projected/' + s + '_proj'
    out_cs = d['data']['out_cs']
    transform = ''
    in_cs = d['data']['in_cs']
    shp_preserve = 'NO_PRESERVE_SHAPE'
    max_dev = ''
    vertical = 'NO_VERTICAL'

    arcpy.Project_management(
        out_layer,
        proj_filename,
        out_cs,
        transform,
        in_cs,
        shp_preserve,
        max_dev,
        vertical,
        )

    arcpy.CopyFeatures_management(out_layer, saved_layer)

    # Save layer to file
    arcpy.SaveToLayerFile_management(out_layer, saved_layer)
