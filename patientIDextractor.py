# import os
# from csv_reader import *
from operator import itemgetter
# from clean_text import *
from dicom_handler import *
from folder_patids_to_csv import *


def Extract(lst):
    list(map(itemgetter(0), lst))  # for first element extraction
    last_element = [item[-1] for item in lst]  # for last element extraction
    return last_element  # return the first line for first element extraction


def pat_id_extractor(path):
    pat_id_list = []
    store_dir_patids = []

    for file in os.listdir(path):
        d = os.path.join(path, file)
        if os.path.isdir(d):
            # print(d)
            x = d.split('\\')
            # print(x[-1])  #returns the patient IDs
            pat_id_list.append(x[-1])
    print("there are",len(pat_id_list), "ids in this source path")
    store_dir_patids = glob.glob(path + '\\*')

    return pat_id_list, store_dir_patids


# to flatten list in a list into a single list
def flatten(l):
    return [item for sublist in l for item in sublist]

    # for it in os.scandir(path):
    #     if it.is_dir():
    #         print(it.path)
    # print(type(it))

