# from dicom_handler import *
# from folder_patids_to_csv import *
# from csv_reader import *
from patientIDextractor import *



if __name__ == '__main__':
    source = "C:\\Users\\shoun\\OneDrive - TUM\\Downloads\\patientdata_yr_19\\19\\"
    #only for testing
    # source = "C:\\Users\\shoun\\OneDrive - TUM\\Downloads\\patientdata_yr_19\\19\\0001074223\\"  # path from where the script reads the dicom files-->ideally a folder having
                                                                                     # several subfolders of different IDs, but can also be tested with a single DICOM file
    destination = "C:\\Users\\shoun\\OneDrive - TUM\\Projects\\outputs\\digibiop\\"  # destination of the output where the sorted files will be stored

    given_list = "C:\\Users\\shoun\\OneDrive - TUM\\Projects\\outputs\\digibiop\\patientID_names_Database_unsorted.csv" #path to the database of the patient names

    # patientIDlist = pat_id_to_csv(source)  #not reqd at the moment
    patientIDlist, patientID_dir = pat_id_extractor(source)
    patientnameslist = csv_read(given_list)  # reads the data from the patient database csv and stores in a variable list

    assert type(patientnameslist) == type(patientIDlist)

    matches = []
    # print(patientnameslist) #prints patient names and IDs from the database
    print("patient ID list in the source folder",'\n', patientIDlist, '\n', type(patientIDlist))
    print("EXTRACT IDs", Extract(patientnameslist), "\n","There are ", len(Extract(patientnameslist)), "patient IDs in the database")


    x = dicom_handler() #initiate the class dicom_handler()
    unsortedList = x.unsortedlist(source)
    # print('unsortedList', unsortedList)
    x.dicom(unsortedList, patientIDlist, patientID_dir, patientnameslist, source, destination)