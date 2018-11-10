import arcpy
import pandas as pd

#returns column names
def get_fc_fields(fc):
    field_names = []
    fields = arcpy.ListFields(fc)
    for field in fields:
        field_names.append(field.name)
    return field_names


#returns column values in dataframe
field_list = get_fc_fields('IND_Landmark_Points_10_26_18_revised')
df = pd.DataFrame([row for row in arcpy.da.SearchCursor(in_fc, field_list)])
    df.columns = field_list

#export to csv
df.to_csv(r'C:\Users\hhernan9\Documents\GitHub\pratt-savi-810-2018-10\students\hhernandez2783\111018\export1.csv')

map_df = arcpy.mapping.ListDataFrame(mxd, layers)[0]
map df

arcpy.mapping.ListDataFrame(map_df)

list_mxd_layer = arcpy.mapping.ListDataFrame(map_df)
list_mxd_layers

#export of multiple layers to csv
for i in list_mxd_layer:
    print i
for i in mxd layers:
    feature_class_to_csv(i,r'C:\Users\hhernan9\Documents\GitHub\pratt-savi-810-2018-10\students\hhernandez2783\111018\export2.csv')


##selects feature
#arcpy.SelectLayerByAttribute_management("nybb", "NEW_SELECTION", """ "boro_name" = 'Manhattan' """)


##zoom to feature and exporting
#mxd = arcpy.mapping.MapDocument('current')
#map_df = arcpy.mapping.ListDataFrames(mxd,"Layers")[0]
#map_df.zoomToSelectedFeatures()
#arcpy.mapping.ExportToPNG(mxd, r'C:\Users\hhernan9\Documents\GitHub\pratt-savi-810-2018-10\students\hhernandez2783\111018\expman1.png')

#steps for above

def export_map_for_feature_in_fc(fc, mxd_file, unique_fieldname, output_png_dir)
#declared mxd as current (intestd of mxd filepath)
mxd = arcpy.mapping.MapDocument('current')

#got my map_dataframe from the mxd objects
map_df = arcpy.mapping.ListDataFrames(mxd,"Layers")[0]

#make empty
list_of_field_values =[]

with arcpy.da.Searchcursor('select_bin_1yr', 'bin') as cursor:
    for row in cursor:
        list_of_field_values.append(row[0])

#for field_value in list_of_field_values: (loop)


    #select
    #zoom
    arcpy.select 'clear selection'
    #export


