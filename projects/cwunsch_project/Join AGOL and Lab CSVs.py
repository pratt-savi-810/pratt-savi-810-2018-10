import pandas as pd
import numpy as np


#  call locations of CSVs
wells_loc = 'E:/GIS/Python/Python/Data REV/AGOL Downloads/Joined Data/Wells_Join.csv'
lab_loc = 'E:/GIS/Python/Python/Data REV/Lab Data CSV/Joined Lab Data/Joined_Lab_Data.csv'


#  allow pandas to read the files
well = pd.read_csv(wells_loc, error_bad_lines=False)
lab = pd.read_csv(lab_loc, error_bad_lines=False)


#  join pc to si by using a dataframe merge
df = pd.merge(well, lab, left_on='Well ID', right_on='StationName', how='left')

list_chem_standards = [
    ["1,4-Dioxane", 0.4],
    ["Vinyl chloride", 0.08],
    ["Ethyl benzene", 1],
    ["Acetone", 4],
    ["Benzene", 1]
]

df['exceed_standards'] = 'did_not_run'


for item in list_chem_standards:
    chem, value_threshold = item[0], item[1]
    df['exceed_standards'] = np.where(
        ((df['ParameterName'] == chem) & (df['Value'] >= value_threshold)),
        'bad',
        np.where(
            (df['exceed_standards'] == 'bad'),
            'bad',
            'okay'
        ),
    )

df = df[['ParameterName', 'Value', 'exceed_standards']]

#  print(len(df.index))

#  convert the data frame to a CSV
df.to_csv('E:/GIS/Python/Python/Data REV/Lab_data_JOINED_AGOL/Wells_Lab_Join_DELETE.csv', index=False)


print(df.head())