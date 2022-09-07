import pydicom as dicom
from patientIDextractor import *
from save_folder_tree import *
from clean_text import *
import numpy as np
from pydicom.fileset import FileSet
import glob


class dicom_handler:
    def __call__(self, *args, **kwargs):
        return None;

    def unsortedlist(self, src, dst):
        unsortedList = []
        directorylist=[]
        for root, dirs, files in os.walk(src):
            # print("root", root)
            # print("dirs", dirs)
            # print("files", files)
            for file in dirs:
                directorylist.append(os.path.join(root, file))
            for file in files:
                #         if ".file" in file:# exclude non-dicoms, good for messy folders
                unsortedList.append(os.path.join(root, file))


        print('%s files found.' % len(unsortedList))
        # print("unsorted list-->", unsortedList)
        # print("directory list-->", directorylist)
        return unsortedList

    def patient_names_extractor(self,patientIDlist, patientnameslist, dst):
        # counter which searches the patient names for their respective IDs
        print("patient_names_extractor called now")
        list=[]
        matches=[]
        for i in range(len(patientIDlist)):

            ls = patientIDlist[i]

            # print("patient_names_extractor running", "\n", "length of patientIDlist=", len(ls), '\n', "length of patientnameslist=", len(patientnameslist))
            # # for i in range(len(patientIDlist)):
            # print("patient_names_extractor running inside loop")
            #
            str_match = [s for s in patientnameslist if ls in s]
            # # folder_patient_name = str(str_match)
            print("str_match", str_match)

            if str_match!= []:
                print("str_match found=", str_match, "\n")
                matches.append(str_match)
            list.append(patientIDlist[i])

        print("matches=", matches)


        print("list=", list)
        print("no. of matches=", len(matches))
        return np.reshape(matches,(6,5)), list


    def str_match_handler(self, patientIDlist, patientnameslist, dst):
            str_match, ls = self.patient_names_extractor(patientIDlist, patientnameslist, dst)
            print("string match handler called", "shape of str_match_handler==>", np.shape(str_match), '\n', str_match)
            ls=[]

            if np.shape(str_match) != (0,):
                print('type of str_match', type(str_match))
                print("folder name",str_match[0][0], str_match[0][1], str_match[0][2])
                print("patientid-->", str_match[0][4] )
                # str_match = str_match[idx:, :]
                # folder_patient_name = str_match[0][0] + '_' + str_match[0][1] + str_match[0][2]
                # print("foldername=", folder_patient_name)
                # np.delete(str_match, (0), axis=0)

                print("str match test", str_match)
                # return folder_patient_name
                return str_match
            else:
                print("no matches found, returning ls-", ls)


            return ls

    def comparator(self, folder_patient_name, matched_patient_id, src):
        matchid=[]
        for i in range(len(matchid)):
            matchid = matched_patient_id[i]

            capture_dir = [patid for patid in src if matchid in src]
            print("captured pat id", capture_dir)
            return capture_dir

    def dicom(self, unsortedList, patientIDlist, patientID_dir, patientnameslist, src, dst):
        # idx = 0
        folder_patient_name_list = self.str_match_handler(patientIDlist, patientnameslist, dst)
        print("folder_patient_name==>", folder_patient_name_list)
        for patient_name in folder_patient_name_list:
            folder_patient_name = patient_name[0] + '_' + patient_name[1] + patient_name[2]
            matched_patient_id = patient_name[4]
            print("foldername and matched patiient id=", folder_patient_name, matched_patient_id)
            self.comparator(folder_patient_name, matched_patient_id, src)

            for dicom_loc in unsortedList:
                # read the file
                print("dicom running")
                ds = dicom.read_file(dicom_loc, force=True)
                # folder_patient_name = self.str_match_handler(patientIDlist, patientnameslist, dst, idx)
                # idx += 1
                # get patient, study, and series information
                # directory = FileSet(ds)
                # print("directory==>", directory)
                patientID = clean_text(ds.get("PatientID", "NA"))
                studyDate = clean_text(ds.get("StudyDate", "NA"))
                studyDescription = clean_text(ds.get("StudyDescription", "NA"))
                seriesDescription = clean_text(ds.get("SeriesDescription", "NA"))
                #     print(type(ds[0x0008, 0x103e])) #<class 'pydicom.dataelem.DataElement'>

                # generate new, standardized file name
                modality = ds.get("Modality", "NA")
                # studyInstanceUID = ds.get("StudyInstanceUID", "NA")

                #     seriesInstanceUID = ds.get("SeriesInstanceUID","NA")
                instanceNumber = str(ds.get("InstanceNumber", "0"))
                fileName = modality + "." + seriesDescription + "." + instanceNumber + '.dcm'
                #     fileName = modality + "." + seriesDescription + "." + instanceNumber + .dcm
                print("filename-", fileName)
                print("folder tree is being called now")
                # if
                #     folder_tree(dst, folder_patient_name, dicom_loc, fileName, patientID, studyDate, studyDescription, seriesDescription)
                #     break
                # folder_patient_name_list = folder_patient_name_list[1:, :]

        print('done')