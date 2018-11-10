import select_bin_ids as sbi

footprints_file = r'C:\Users\pjarymow\Documents\ArcMap_Data\data\LPC_IL_HD_Bld_DB_10_19_18.shp'

input_bin = '1011258'

distance = '400 Feet'

bin_ids = sbi.select_bin_ids(input_bin, footprints_file, distance)

print('checkpoint')

print(bin_ids)
