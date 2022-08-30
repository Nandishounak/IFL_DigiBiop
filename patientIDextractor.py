import os
from csv_reader import *
import numpy as np
from operator import itemgetter


def Extract(lst):
    list(map(itemgetter(0), lst)) #for first element extraction
    last_element = [item[-1] for item in lst] #for last element extraction
    return last_element #return the first line for first element extraction

def pat_id_extractor(path):
    pat_id_list=[]
    for file in os.listdir(path):
        d = os.path.join(path, file)
        if os.path.isdir(d):
            # print(d)
            x = d.split('\\')
            print(x[-1])
            pat_id_list.append(x[-1])
    print(np.shape(pat_id_list))
    return pat_id_list


    # for it in os.scandir(path):
    #     if it.is_dir():
    #         print(it.path)
    # print(type(it))


if __name__ == '__main__':
    patientIDlist = pat_id_extractor("C:\\Users\\shoun\\OneDrive - TUM\\Downloads\\patientdata_yr_19\\19\\")
    given_list = "C:\\Users\\shoun\\OneDrive - TUM\\Projects\\outputs\\digibiop\\patientID_names_Database_unsorted.csv"
    patientnameslist = csv_read(given_list) #reads the data from the patient database csv and stores in a variable list

    assert type(patientnameslist)==type(patientIDlist)

    matches = []
    print(patientnameslist)
    print("EXTRACT IDs", Extract(patientnameslist))

    # for match in ls:
    #     if patientIDlist[5] in match:
    #         matches.append(match)
    #
    # print("matches",matches)

    #counter which searches the patient names for their respective IDs
    for i in range(len(patientIDlist)):
        ls = patientIDlist[i]

        str_match = [s for s in patientnameslist if ls in s]
        print('str_match', str_match)

