import pandas as pd
import glob
import csv
import numpy as np
import arcpy
arcpy.CheckOutExtension("Spatial")


data_dir = 'D:/GIS/Python/Python/Data REV/AGOL Downloads'

purge_chemistry = '{}/Purge Chemistry.csv'.format(data_dir)
sampling_info = '{}/Sampling Info.csv'.format(data_dir)
wells = '{}/Wells.csv'.format(data_dir)


pc = pd.read_csv(purge_chemistry)
si = pd.read_csv(sampling_info)
well = pd.read_csv(wells)

df = pc.merge(si,
              left_on='Well ID',
              right_on='Well Number',
              how='left'
              )

df.to_csv('D:/GIS/Python/Python/Data REV/AGOL Downloads/Joined Data/PC_SI_JoinPROJECT.csv'.format(data_dir),
          index=False
          )

PC_SI_Join = 'D:/GIS/Python/Python/Data REV/AGOL Downloads/Joined Data/PC_SI_JoinPROJECT.csv'.format(data_dir)

join1 = pd.read_csv(PC_SI_Join)

df = well.merge(join1,
                left_on='Well ID',
                right_on='Well ID',
                how='left'
                )

df.to_csv('D:/GIS/Python/Python/Data REV/AGOL Downloads/Joined Data/Wells_JoinPROJECT.csv'.format(data_dir),
          index=False
          )

csvfile = glob.glob('D:\GIS\Python\Python\Data REV\Lab Data CSV\*.csv')
wf = csv.writer(open('D:\GIS\Python\Python\Data REV\Lab Data CSV\Joined Lab Data\Joined_Lab_DataPROJECT.csv', 'wb'),
                delimiter = ','
                )
f1 = 'D:\GIS\Python\Python\Data REV\Lab Data CSV\Joined Lab Data\Joined_Lab_DataPROJECT.csv'

for file in csvfile:
    #  print files
    rd = csv.reader(open(file, 'r'), delimiter = ',')
    rd.next()
    for row in rd:
        print row
        wf.writerow(row)

header_saved = False
with open(f1, 'wb') as fout:
    for filename in csvfile:
        with open(filename) as fin:
            header = next(fin)
            if not header_saved:
                fout.write(header)
                header_saved = True
            for line in fin:
                fout.write(line)

wells_loc = 'D:/GIS/Python/Python/Data REV/AGOL Downloads/Wells.csv'
lab_loc = 'D:/GIS/Python/Python/Data REV/Lab Data CSV/Joined Lab Data/Joined_Lab_DataPROJECT.csv'

well = pd.read_csv(wells_loc,
                   error_bad_lines=False
                   )
lab = pd.read_csv(lab_loc,
                  error_bad_lines=False
                  )

df = pd.merge(well,
              lab,
              left_on='Well ID',
              right_on='StationName',
              how='left'
              )

list_chem_standards = [
    ["Benzene", 1],
    ["Tetrachloroethene", 1],
    ["Trichloroethene", 1],
    ["1,2-Dichloroethane", 2],
    ["1,4-Dioxane", 0.4]
]

df['exceed_standards'] = 'did_not_run'

for item in list_chem_standards:
    chem, value_threshold = item[0], item[1]
    df['exceed_standards'] = np.where(
        ((df['ParameterName'] == chem) & (df['Value'] >= value_threshold)),
        'exceed',
        np.where(
            (df['exceed_standards'] == 'exceed'),
            'exceed',
            'good'
        ),
    )

df = df[['Well ID',
         'SampleMatrix',
         'ParameterName',
         'Value',
         'ReportingUnits',
         'exceed_standards',
         'AnalyticMethod',
         'FlagCode',
         'Detect2',
         'SampleDate_D',
         'LimitType',
         'DilutionFactor',
         'LabSampleID',
         'X',
         'Y']
]

df.to_csv('D:/GIS/Python/Python/Data REV/Lab_data_JOINED_AGOL/Wells_Lab_Join_FLAGPROJECT.csv',
          index=False
          )

out_folder_path = "D:/GIS/Python/Python/Data REV/GDB"
out_name = "GW_ResultsPROJECT.gdb"

arcpy.CreateFileGDB_management(out_folder_path,
                               out_name
                               )

arcpy.env.workspace = "D:/GIS/Python/Python/Data REV/GDB/GW_ResultsPROJECT.gdb"


in_table = "D:/GIS/Python/Python/Data REV/Lab_data_JOINED_AGOL/Wells_Lab_Join.csv"
in_table_2 = "D:/GIS/Python/Python/Data REV/Lab_data_JOINED_AGOL/Wells_Lab_Join_FLAG.csv"

arcpy.MakeXYEventLayer_management(
    in_table,
    'X',
    'Y',
    'XY_plot'
)

arcpy.CopyFeatures_management(
    'XY_plot',
    'D:/GIS/Python/Python/Data REV/SHP/GW_ResultsPROJECT.shp'
)

arcpy.MakeXYEventLayer_management(
    in_table_2,
    'X',
    'Y',
    'XY_plot2'
)

arcpy.CopyFeatures_management(
    'XY_plot2',
    'D:/GIS/Python/Python/Data REV/SHP/GW_Results_FlagPROJECT.shp'
)

arcpy.FeatureClassToGeodatabase_conversion ('D:/GIS/Python/Python/Data REV/SHP/GW_ResultsPROJECT.shp',
                                            'D:/GIS/Python/Python/Data REV/GDB/GW_ResultsPROJECT.gdb'
                                            )

arcpy.FeatureClassToGeodatabase_conversion ('D:/GIS/Python/Python/Data REV/SHP/GW_Results_FlagPROJECT.shp',
                                            'D:/GIS/Python/Python/Data REV/GDB/GW_ResultsPROJECT.gdb'
                                            )

arcpy.env.workspace = "D:/GIS/Python/Python/Data REV/SHP"
fc = "D:/GIS/Python/Python/Data REV/SHP/GW_Results_FlagPROJECT.shp"
query = '"exceed_sta" = \'exceed\''
fc2 = "D:/GIS/Python/Python/Data REV/SHP/Exceedance_Locations.shp"
query2 = '"ParameterN" = \'Benzene\''

arcpy.MakeFeatureLayer_management(fc,
                                  "f_lyr"
                                  )

exceedance = arcpy.SelectLayerByAttribute_management("f_lyr",
                                                     "NEW_SELECTION",
                                                     query
                                                     )

arcpy.CopyFeatures_management (exceedance,
                               'D:/GIS/Python/Python/Data REV/SHP/Exceedance_Locations.shp'
                               )

arcpy.FeatureClassToGeodatabase_conversion ('D:/GIS/Python/Python/Data REV/SHP/Exceedance_Locations.shp',
                                           'D:/GIS/Python/Python/Data REV/GDB/GW_ResultsPROJECT.gdb'
                                            )

arcpy.MakeFeatureLayer_management (fc2,
                                   "f_lyr2"
                                   )

benzene_exceedance = arcpy.SelectLayerByAttribute_management("f_lyr2",
                                                             "NEW_SELECTION",
                                                             query2
                                                             )

arcpy.CopyFeatures_management (benzene_exceedance, 'D:/GIS/Python/Python/Data REV/SHP/Benzene_Exceedances.shp')

arcpy.FeatureClassToGeodatabase_conversion ('D:/GIS/Python/Python/Data REV/SHP/Benzene_Exceedances.shp',
                                            'D:/GIS/Python/Python/Data REV/GDB/GW_ResultsPROJECT.gdb'
                                            )

arcpy.gp.Idw_sa("D:/GIS/Python/Python/Data REV/GDB/GW_ResultsPROJECT.gdb/Benzene_Exceedances.shp",
                "Value",
                "D:/GIS/Python/Python/Data REV/GDB/GW_ResultsPROJECT.gdb/Idw_Benzene_1",
                "7.34925976075829E-07",
                "2",
                "VARIABLE 12"
                )



