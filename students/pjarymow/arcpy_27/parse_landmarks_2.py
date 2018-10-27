import pandas as pd
# import arcpy

# create dataframe variable
in_csv = 'C:/Users/pjarymow/Documents/GitHub/pratt-savi-810-2018-10/students/pjarymow/arcpy_27/data-10_27_2018/LPC_LL_OpenData_2015Nov.csv'
df = pd.read_csv(in_csv)

# print(df.head(10))

df_MN = df[(df['BoroughID'] == 'MN')]  # query to only select borough ID manhattan

print('All Landmarks Count: ' + len(df.index).__str__())

print('Manhattan Landmarks Count: ' + len(df_MN.index).__str__())

print('Count of Historic Landmarks by District in Manhattan')

dfg = df.groupby(['LM_NAME'], as_index=False).count()

