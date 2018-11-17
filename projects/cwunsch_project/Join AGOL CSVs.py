import pandas as pd

data_dir = 'E:/GIS/Python/Python/Data REV/AGOL Downloads'

purge_chemistry = '{}/Purge Chemistry.csv'.format(data_dir)
sampling_info = '{}/Sampling Info.csv'.format(data_dir)
wells = '{}/Wells.csv'.format(data_dir)


pc = pd.read_csv(purge_chemistry, error_bad_lines=False)
si = pd.read_csv(sampling_info, error_bad_lines=False)
well = pd.read_csv(wells, error_bad_lines=False)


df = pc.merge(si, left_on='Well ID', right_on='Well Number', how='left')


df.to_csv('E:/GIS/Python/Python/Data REV/AGOL Downloads/Joined Data/PC_SI_Join.csv'.format(data_dir), index=False)


PC_SI_Join = 'E:/GIS/Python/Python/Data REV/AGOL Downloads/Joined Data/PC_SI_Join.csv'.format(data_dir)


join1 = pd.read_csv(PC_SI_Join, error_bad_lines=False)


print(df.head())


df = well.merge(join1, left_on='Well ID', right_on='Well ID', how='left')


df.to_csv('E:/GIS/Python/Python/Data REV/AGOL Downloads/Joined Data/Wells_Join.csv'.format(data_dir), index=False)