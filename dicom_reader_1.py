import os
# import csv
# import imfusion
import pydicom as dicom
from pydicom.fileset import FileSet
import  pathlib
import numpy as np
from pathlib import Path
import dicom_csv
from dicom_csv import join_tree


path= pathlib.PurePosixPath('/mnt/projects/DeepProstateDB/Data/14/0001330324/DICOMDIR')

folder = '/mnt/HDD1/shounak/Biopsy_output/0002298177'
meta = join_tree(folder, verbose=2)
meta.head[2]
ds = dicom.dcmread(path)
file = FileSet(ds)
print(file)

# test_read=dicom.read_file(ds)
seriesdesc = file.find_values("Pelvis")
print(seriesdesc)
# print(ds.DirectoryRecordSequence[0x0018, 0x103e].value)
# print(ds[0x0018, 0x103e].value)
# print(test_read[0x0018, 0x4158])

#
# imfusion.init()
# imfusion.open('EE0A13C6')