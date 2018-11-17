import pandas as pd


#  call locations of CSVs
wells_loc = 'E:/GIS/Python/Python/Data/CSV/Wells_Join.csv'
lab_loc = 'E:/GIS/Python/Python/Data/Result Data CSV/RAW/combinedrev_new.csv'


#  allow pandas to read the files
well = pd.read_csv(wells_loc)
lab = pd.read_csv(lab_loc)


#  join pc to si by using a dataframe merge
df = well.merge(lab, left_on='Well ID', right_on='StationName', how='left')


#  print(len(df.index))

#  convert the data frame to a CSV
df.to_csv('E:/GIS/Python/Python/Data/Well and Lab Join/join_output.csv', index=False)


print(df.head())


