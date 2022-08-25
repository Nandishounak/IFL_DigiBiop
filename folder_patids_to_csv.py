import os
import csv


#testing with a directory
#windows
path = os.path.dirname("C:\\Users\\shoun\\OneDrive - TUM\\Downloads\\19\\19\\")

#linus-iflpc
# path=os.path.dirname("/mnt/projects/DeepProstateDB/Data/14/0001147395(multiple_times_of_scan)/README.txt")

print(path)
print(os.path.basename(path))

#windows
my_list = os.listdir("C:\\Users\\shoun\\OneDrive - TUM\\Downloads\\19\\19\\")

#linux-iflpc
# my_list = os.listdir("/mnt/projects/DeepProstateDB/Data/14/")
print(my_list)

# sends the output to the csv file
#windows
with open('Z:\\Projects\\unsorted data\\patientids.csv', 'w', newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(my_list)

#linux
# with open('/mnt/HDD1/shounak/patientids.csv', 'w', newline='') as myfile:
#     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
#     wr.writerow(my_list)
