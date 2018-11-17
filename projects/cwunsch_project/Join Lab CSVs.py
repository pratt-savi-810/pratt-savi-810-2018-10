import glob
import csv


csvfile = glob.glob('E:\GIS\Python\Python\Data REV\Lab Data CSV\*.csv')
wf = csv.writer(open('E:\GIS\Python\Python\Data REV\Lab Data CSV\Joined Lab Data\Joined_Lab_Data.csv', 'wb'), delimiter = ',')

for file in csvfile:
    #  print files
    rd = csv.reader(open(file, 'r'), delimiter = ',')
    rd.next()
    for row in rd:
        print row
        wf.writerow(row)

header_saved = False
with open('E:\GIS\Python\Python\Data REV\Lab Data CSV\Joined Lab Data\Joined_Lab_Data.csv','wb') as fout:
    for filename in csvfile:
        with open(filename) as fin:
            header = next(fin)
            if not header_saved:
                fout.write(header)
                header_saved = True
            for line in fin:
                fout.write(line)