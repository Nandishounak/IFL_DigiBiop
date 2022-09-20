import pydicom as dicom
from patientIDextractor import *
from save_folder_tree import *
from clean_text import *
import numpy as np
from pydicom.fileset import FileSet



class dicom_handler:
    def __call__(self, *args, **kwargs):
        return None;

    def unsortedlist(self, src):
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

    def search_patid_in_dir(self, directory, matched_patient_id):
        print("search_patid_in_dir is working now")

        for fname in directory:
            # f = open(directory+matched_patient_id, 'r')
            # f.close()

            print("matched patient ID>>>>", matched_patient_id, directory)
            if matched_patient_id in os.listdir(directory):
                print("found string in file", os.listdir(directory))
                # print("i should know swhats this", Path(directory + matched_patient_id))
                list_of_matched_name = self.unsortedlist(directory + matched_patient_id)
                return list_of_matched_name
            else:
                return None
    def patient_names_extractor(self,patientIDlist, patientnameslist, dst):
        # counter which searches the patient names for their respective IDs
        print("patient_names_extractor called now")
        list=[]
        matches=[]
        # patientnameslist=['a/1', 'b/2', 'c/3', 'd/4']
        # patientIDlist= ['1','2']
        for i in range(len(patientIDlist)):

            ls = patientIDlist[i]
            # print ("ls",type(ls))
            # print("patientnameslist", patientnameslist)
            # print("patientIDlist", patientIDlist)


        # print("patient_names_extractor running", "\n", "length of patientIDlist=", len(ls), '\n', "length of patientnameslist=", len(patientnameslist))
            # # for i in range(len(patientIDlist)):
            # print("patient_names_extractor running inside loop")
            #

            # for s in patientnameslist:
            #     if ls in s:
            #         str_match=s
            str_match = [s for s in patientnameslist if ls in s]
            # # folder_patient_name = str(str_match)
            # print("str_match", str_match)


            if str_match!= []:
                print("str_match found=", str_match, "\n")
                matches.append(str_match)
            list.append(patientIDlist[i])

        print("matches=", matches, '\n', np.shape(matches))
        # match_reshaped= matches


        print("list=", list)
        print("no. of matches=", len(matches))
        return np.reshape(matches,(len(matches), 5)), list


    def str_match_handler(self, patientIDlist, patientnameslist, dst):
            str_match, ls = self.patient_names_extractor(patientIDlist, patientnameslist, dst)
            print("string match handler called....shape of str_match_handler==>", np.shape(str_match))
            ls=[]

            if np.shape(str_match) != (0, 5):   #the shape depends on the number of columns present in the csv file. Since I have created an extra coulumn, it is (1,5). otherwise it would have been 4, 3 coulmns for name and 1 for patient ID
                # print('type of str_match', type(str_match))     #<class 'numpy.ndarray'>


                print("str match(matched patient names and ids)","\n", str_match)
                # return folder_patient_name
                return str_match
            else:
                print("no matches found, check for duplicate entries....returning...", ls)


            return ls

    def comparator(self, folder_patient_name, matched_patient_id, src):

        print("matched_patient_id-->", matched_patient_id)

        matchid = matched_patient_id
        print("len matchid", len(matched_patient_id))
        capture_dir = [patid for patid in src if matchid in src]
        print("captured pat id", capture_dir)
        return capture_dir

    def patient_info_segregator(self, dicom_loc):
        ds = dicom.read_file(dicom_loc, force=True)

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
        # print("filename-", fileName)

        return ds, dicom_loc, fileName, patientID, studyDate, studyDescription, seriesDescription

    def dicom(self, unsortedList, patientIDlist, patientID_dir, patientnameslist, src, dst):

        folder_patient_name_list = self.str_match_handler(patientIDlist, patientnameslist, dst)
        # print("folder_patient_name==>", folder_patient_name_list)
        for patient_name in folder_patient_name_list:
            folder_patient_name = patient_name[0] + '_' + patient_name[1] + patient_name[2]
            matched_patient_id = patient_name[4]
            print("foldername and matched patiient id=", folder_patient_name, matched_patient_id)
            # self.comparator(folder_patient_name, matched_patient_id, src)
            matched_directory = self.search_patid_in_dir(src, matched_patient_id)
            if matched_directory != None:
                for dicom_loc in matched_directory:
                    print("I am reading from matched directory")
                    ds, dicom_loc, fileName, patientID, studyDate, studyDescription, seriesDescription= self.patient_info_segregator(dicom_loc)
                    folder_tree(ds, dst, folder_patient_name, dicom_loc, fileName, patientID, studyDate,
                                studyDescription, seriesDescription)

                    # print("dicom_loc, fileName, patientID, studyDate, studyDescription, seriesDescription=", dicom_loc, fileName, patientID, studyDate, studyDescription, seriesDescription)

            else:
                for dicom_loc in unsortedList:
                    ds, dicom_loc, fileName, patientID, studyDate, studyDescription, seriesDescription= self.patient_info_segregator(dicom_loc)
                    print("dicom running for unsorted list where match is not found")

                print("folder tree is being called now")
            # if folder_patient_name != []:
            #     folder_tree(ds, dst, folder_patient_name, dicom_loc, fileName, patientID, studyDate, studyDescription, seriesDescription)
            #     break
            # folder_patient_name_list = folder_patient_name_list[1:, :]

        print('done')