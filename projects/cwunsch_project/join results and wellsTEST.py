import csv
from collections import OrderedDict

with open('E:/GIS/Python/Python/Data/CSV/Wells_Join.csv', 'rb') as f:
    r = csv.reader(f)
    dict2 = {row[0]: row[1:] for row in r}

with open('E:/GIS/Python/Python/Data/Result Data CSV/RAW/combinedrev_new.csv', 'rb') as f:
    r = csv.reader(f)
    dict1 = OrderedDict((row[0], row[1:]) for row in r)

result = OrderedDict()
for d in (dict1, dict2):
    for key, value in d.iteritems():
         result.setdefault(key, []).extend(value)

with open('E:/GIS/Python/Python/Data/Well and Lab Join/join_output.csv', 'wb') as f:
    w = csv.writer(f)
    for key, value in result.iteritems():
        w.writerow([key] + value)