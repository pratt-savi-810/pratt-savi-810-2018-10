import pandas as pd

#  call data directory location
data_dir = 'C:/Users/cwunsch/Desktop/Python/Data/CSV'

#  call locations of CSVs. Squigly brackets indicate the data directory above.
purge_chemistry = '{}/Purge Chemistry.csv'.format(data_dir)
sampling_info = '{}/Sampling Info.csv'.format(data_dir)
wells = '{}/Wells.csv'.format(data_dir)

#  allow pandas to read the files
pc = pd.read_csv(purge_chemistry)
si = pd.read_csv(sampling_info)
well = pd.read_csv(wells)

#  join pc to si by using a dataframe merge
df = pc.merge(si, left_on='Well ID', right_on='Well Number', how='left')

#  print(df.head())

#  print(len(df.index))

#  convert the data frame to a CSV
df.to_csv('{}/PC_SI_Join.csv'.format(data_dir), index=False)


#  call the new location of the newly joined CSV
PC_SI_Join = '{}/PC_SI_Join.csv'.format(data_dir)

#  allow pandas to read the file
join1 = pd.read_csv(PC_SI_Join)


print(df.head())

#  join the previously joined CSV to the wells CSV
df = well.merge(join1, left_on='Well ID', right_on='Well ID', how='left')

#  convert the data frame to a CSV
df.to_csv('{}/Wells_Join.csv'.format(data_dir), index=False)




