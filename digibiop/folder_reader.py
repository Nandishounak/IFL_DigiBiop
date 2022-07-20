import os
import csv
import imfusion


# os.environ['PATH'] = '/usr/include/ImFusion/Ext/Eigen/src/plugins;/usr/include/ImFusion;' + os.environ['PATH']
# # os.environ['PYTHONPATH'] = os.environ['PYTHONPATH'] + ';C:\\Program Files\\ImFusion\\ImFusion Suite\\Suite;'
# PYTHONUNBUFFERED=1

path=os.path.dirname("/mnt/projects/DeepProstateDB/Data/14/0001147395(multiple_times_of_scan)/README.txt")
print(path)
print(os.path.basename(path))

my_list = os.listdir("/mnt/projects/DeepProstateDB/Data/14/")
print(my_list)
with open('/mnt/HDD1/shounak/patientids.csv', 'w', newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(my_list)
