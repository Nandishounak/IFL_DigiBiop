import csv


def csv_read(path):
    with open(path, newline='') as csvfile: #for windows
        xyz= csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in xyz:
            print(', '.join(row))
    return None