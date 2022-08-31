import os
from csv_reader import *
from operator import itemgetter
from clean_text import *
from dicom_handler import *
from folder_patids_to_csv import *


def Extract(lst):
    list(map(itemgetter(0), lst))  # for first element extraction
    last_element = [item[-1] for item in lst]  # for last element extraction
    return last_element  # return the first line for first element extraction


def pat_id_extractor(path):
    pat_id_list = []
    for file in os.listdir(path):
        d = os.path.join(path, file)
        if os.path.isdir(d):
            # print(d)
            x = d.split('\\')
            # print(x[-1])  #returns the patient IDs
            pat_id_list.append(x[-1])
    print("there are",len(pat_id_list), "ids in this source path")
    return pat_id_list


# to flatten list in a list into a single list
def flatten(l):
    return [item for sublist in l for item in sublist]

    # for it in os.scandir(path):
    #     if it.is_dir():
    #         print(it.path)
    # print(type(it))


if __name__ == '__main__':
    source = "C:\\Users\\shoun\\OneDrive - TUM\\Downloads\\patientdata_yr_19\\19\\"
    #only for testing
    # source = "C:\\Users\\shoun\\OneDrive - TUM\\Downloads\\patientdata_yr_19\\19\\0001074223\\"  # path from where the script reads the dicom files-->ideally a folder having
                                                                                     # several subfolders of different IDs, but can also be tested with a single DICOM file
    destination = "C:\\Users\\shoun\\OneDrive - TUM\\Projects\\outputs\\digibiop\\"  # destination of the output where the sorted files will be stored

    given_list = "C:\\Users\\shoun\\OneDrive - TUM\\Projects\\outputs\\digibiop\\patientID_names_Database_unsorted.csv" #path to the database of the patient names

    # patientIDlist = pat_id_to_csv(source)  #not reqd at the moment
    patientIDlist = pat_id_extractor(source)
    patientnameslist = csv_read(given_list)  # reads the data from the patient database csv and stores in a variable list

    assert type(patientnameslist) == type(patientIDlist)

    matches = []
    # print(patientnameslist) #prints patient names and IDs from the database
    print("patient ID list in the source folder",'\n', patientIDlist, '\n', type(patientIDlist))
    print("EXTRACT IDs", Extract(patientnameslist), "\n","There are ", len(Extract(patientnameslist)), "patient IDs in the database")

    # counter which searches the patient names for their respective IDs
    # for i in range(len(patientIDlist)):
    #     ls = patientIDlist[i]
    #
    #     str_match = [s for s in patientnameslist if ls in s]
    #     if np.shape(str_match)!= (0,):
    #         print('str_match', str_match)
    #         print(str_match[0][0], str_match[0][1], str_match[0][2])
    #########################################

    x = dicom_handler() #initiate the class dicom_handler()
    unsortedList = x.unsortedlist(source, destination)
    # print('unsortedList', unsortedList)
    x.dicom(unsortedList, patientIDlist, patientnameslist, destination)
