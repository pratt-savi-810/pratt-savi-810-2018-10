

import csv


with open('C:/Users/Riches/Desktop/CRA/CRANALITICS/phycharm/Cartel1.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=';')

    names = []
    address = []

    for row in readCSV:

       name = row[0]
       addresses = row[2]

       names.append(name)
       address.append(addresses)


    print(names)
    print(address)





