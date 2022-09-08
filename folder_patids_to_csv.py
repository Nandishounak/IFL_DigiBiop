import os
import csv


#testing with a directory
def pat_id_to_csv(path):
    #windows
    # path = os.path.dirname("C:\\Users\\shoun\\OneDrive - TUM\\Downloads\\patientdata_yr_19\\19\\")

    #linus-iflpc
    # path=os.path.dirname("/mnt/projects/DeepProstateDB/Data/14/0001147395(multiple_times_of_scan)/README.txt")

    print(path)
    print(os.path.basename(path))

    #windows
    my_list = os.listdir(path)

    #linux-iflpc
    # my_list = os.listdir("/mnt/projects/DeepProstateDB/Data/14/")
    print('patlist->',my_list, '\n', type(my_list))

    # sends the output to the csv file
    #windows
    with open('C:\\Users\\shoun\\OneDrive - TUM\\Projects\\outputs\\digibiop\\patientids.csv', 'w', newline='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(my_list)
    print(my_list)

    #linux
    # with open('/mnt/HDD1/shounak/patientids.csv', 'w', newline='') as myfile:
    #     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    #     wr.writerow(my_list)
