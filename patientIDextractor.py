import os
from csv_reader import *

def pat_id_extractor(path):
    pat_id_list=[]
    for file in os.listdir(path):
        d=os.path.join(path, file)
        if os.path.isdir(d):
            # print(d)
            x = d.split('\\')
            print(x[-1])
            pat_id_list.append(x[-1])
    print(pat_id_list)


    # for it in os.scandir(path):
    #     if it.is_dir():
    #         print(it.path)
    # print(type(it))


if __name__ == '__main__':
    pat_id_extractor("C:\\Users\\shoun\\OneDrive - TUM\\Downloads\\patientdata_yr_19\\19\\")
    given_list = "C:\\Users\\shoun\\OneDrive - TUM\\Projects\\outputs\\digibiop\\patientID_names_Database_unsorted.csv"
    csv_read(given_list)