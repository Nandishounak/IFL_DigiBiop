#This script only reads .csv and will throw encoding error for .xlsx files
import csv
import numpy as np


def csv_read(path):
    mycsvlist=[]
    with open(path, encoding="ISO-8859-1", newline='') as csvfile: #for windows
        xyz= csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in xyz:
            # print(', '.join(row))
            # print(type(row))
            mycsvlist.append(row)

    print(mycsvlist, '\n')
    return mycsvlist
