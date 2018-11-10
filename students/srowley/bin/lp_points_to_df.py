import arcpy
import pandas as pd

#get feature class field names
def get_fc_fields(fc):
    field_names = []
    fields = arcpy.ListFields(fc)
    for field in fields:
        field_names.append(field.name)
    return field_names


field_list = get_fc_fields(in_fc)
for row in arcpy.da.SearchCursor(in_fc, field_list):
    print(row)
    df = pd.DataFrame([row for row in arcpy.da.SearchCursor(in_fc, field_list)])
   return df
    #columns as property of fields, set to field_list
    df.columns = field_list
    return df
   # export to csv
df.to_csv(r'C:\Users\srowley4\Documents\GitHub\pratt-savi-810-2018-10\students\srowley\bin\new.csv', encoding='utf-8')

map_df = arcpy.mapping.ListDataFrame(mxd, layers)[0]
map_df

arcpy.mapping.ListDataFrame(map_df)

list_mxd_layer = arcpy.mapping.ListDataFrame(map_df)
list_mxd_layers

for i in list_mxd_layers:
    print i
for i in mxd layers:
        feature_class_to_csv(i,r'C:\Users\srowley4\Documents\GitHub\pratt-savi-810-2018-10\students\srowley\bin\new.csv'.format(i), encoding='utf-8')
        list_mxd_layers


#export map or each borough
arcpy.SelectLayerByAttribute_management("nybb", "new_selection", """ "boro_name" = 'Manhattan'""")
<Result 'nybb'>
#return
mxd = arcpy.mapping.MapDocument('CURRENT')
return mxd
map_df = arcpy.mapping.ListDataFrames(mxd, "Layers")[0]
map_df.zoomToSelectedFeatures()
arcpy.mapping.EportToPNG(mxd,r'C:\Users\srowley4\Documents\GitHub\pratt-savi-810-2018-10\students\srowley\bin\new2.png, encoding='utf-8')



def export_map_for_feature_in_fc(fc, mxd_file,uniques_fieldname)
mxd = arcpy.mapping.MapDocument(mxd_file)
#Got mapdatafame from mxd object
map_df = arcpy.mapping.listDatFrames(mxd, "*")[0]
#make empty
list of field values=[]
with arcpy.da.SearchCursor(fc, unique_fieldname) as cursor:
    for row in cursor:
        list_of_fields.append(row[0])
for field_value in List_of_field_value:
arcpy.selectLayerByAtribute_management(
    fc,
    "new_selection"
    """ "{}" = '{}' """.format(unique_fieldname, field_value),
)
map_df.zoomToSelectedFeatures()
arcpy.RefreshAciveView()

arcpy.mapping.EportToPNG(mdx, '{}_{}.png'.format(output_png_dir, field_values))