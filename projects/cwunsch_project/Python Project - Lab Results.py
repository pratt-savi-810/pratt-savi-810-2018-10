import glob
import csv


csvfile = glob.glob('C:\Users\cwunsch\Desktop\Python\Data\Result Data CSV\RAW\*.csv')
wf = csv.writer(open('C:\Users\cwunsch\Desktop\Python\Data\Result Data CSV\RAW\combinedrev_new.csv', 'wb'), delimiter = ',')

for file in csvfile:
    #  print files
    rd = csv.reader(open(file, 'r'), delimiter = ',')
    rd.next()
    for row in rd:
        print row
        wf.writerow(row)

header_saved = False
with open('C:\Users\cwunsch\Desktop\Python\Data\Result Data CSV\RAW\combinedrev_new.csv','wb') as fout:
    for filename in csvfile:
        with open(filename) as fin:
            header = next(fin)
            if not header_saved:
                fout.write(header)
                header_saved = True
            for line in fin:
                fout.write(line)