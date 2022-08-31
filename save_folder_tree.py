import os
import pydicom as dicom


def folder_tree(dst, folder_patient_name, dicom_loc, fileName, patientID, studyDate, studyDescription,
                seriesDescription):
    # save files to a 4-tier nested folder structure
    print("folder tree running now")
    ds = dicom.read_file(dicom_loc, force=True)
    if os.path.exists(os.path.join(dst, folder_patient_name, "na")):
        pass
    if not os.path.exists(os.path.join(dst, folder_patient_name)):
        os.makedirs(os.path.join(dst, folder_patient_name))

    if not os.path.exists(os.path.join(dst, patientID)):
        os.makedirs(os.path.join(dst, folder_patient_name, patientID))
    if not os.path.exists(os.path.join(dst, folder_patient_name, patientID, studyDate)):
        os.makedirs(os.path.join(dst, folder_patient_name, patientID, studyDate))
    if not os.path.exists(os.path.join(dst, folder_patient_name, patientID, studyDate, studyDescription)):
        os.makedirs(os.path.join(dst, folder_patient_name, patientID, studyDate, studyDescription))
    if not os.path.exists(
        os.path.join(dst, folder_patient_name, patientID, studyDate, studyDescription, seriesDescription)):
        os.makedirs(os.path.join(dst, folder_patient_name, patientID, studyDate, studyDescription, seriesDescription))
    print('Saving out file: %s - %s - %s - %s - %s.' % (folder_patient_name, patientID, studyDate, studyDescription, seriesDescription))
    return ds.save_as(os.path.join(dst, folder_patient_name, patientID, studyDate, studyDescription, seriesDescription, fileName))
