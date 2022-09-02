import pydicom as dicom
from patientIDextractor import *
from save_folder_tree import *
from clean_text import *


class dicom_handler:
    def __call__(self, *args, **kwargs):
        return None;

    def unsortedlist(self, src, dst):
        unsortedList = []
        for root, dirs, files in os.walk(src):
            # print("root", root)
            # print("dirs", dirs)
            # print("files", files)
            for file in files:
                #         if ".file" in file:# exclude non-dicoms, good for messy folders
                unsortedList.append(os.path.join(root, file))

        print('%s files found.' % len(unsortedList))
        return unsortedList

    def patient_names_extractor(self,patientIDlist, patientnameslist, dst):
        # counter which searches the patient names for their respective IDs
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
            # print("str_match", str_match)

            if str_match!= []:
                print("str_match found=", str_match, "\n")
                matches.append(str_match)
        # return str_match


            list.append(patientIDlist[i])
        print("list=", list)
        print("no. of matches=", len(matches))

    def str_match_handler(self, patientIDlist, patientnameslist, dst):
            str_match = self.patient_names_extractor(patientIDlist, patientnameslist, dst)
            print(np.shape(str_match))
            # if np.shape(str_match) != (0,):
            #     print('str_match', str_match)
            #     print(str_match[0][0], str_match[0][1], str_match[0][2])
            #     folder_patient_name = str_match[0][0] + '_' + str_match[0][1] + str_match[0][2]
            #     return folder_patient_name
            # # else:
            #     ls = str(patientIDlist[i])
            #     print("ls", ls)
            #
            #
            # return ls

    def dicom(self, unsortedList, patientIDlist, patientnameslist, dst):
        for dicom_loc in unsortedList:
            # read the file
            print("dicom running")
            ds = dicom.read_file(dicom_loc, force=True)
            folder_patient_name = self.str_match_handler(patientIDlist, patientnameslist, dst)
            # get patient, study, and series information
            patientID = clean_text(ds.get("PatientID", "NA"))
            studyDate = clean_text(ds.get("StudyDate", "NA"))
            studyDescription = clean_text(ds.get("StudyDescription", "NA"))
            seriesDescription = clean_text(ds.get("SeriesDescription", "NA"))
            #     print(type(ds[0x0008, 0x103e])) #<class 'pydicom.dataelem.DataElement'>

            # generate new, standardized file name
            modality = ds.get("Modality", "NA")
            studyInstanceUID = ds.get("StudyInstanceUID", "NA")

            #     seriesInstanceUID = ds.get("SeriesInstanceUID","NA")
            instanceNumber = str(ds.get("InstanceNumber", "0"))
            fileName = modality + "." + seriesDescription + "." + instanceNumber + '.dcm'
            #     fileName = modality + "." + seriesDescription + "." + instanceNumber + .dcm
            print(fileName)
            print("folder tree is being called now")
            folder_tree(dst, folder_patient_name, dicom_loc, fileName, patientID, studyDate, studyDescription, seriesDescription)
        print('done')