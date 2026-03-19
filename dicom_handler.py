"""DICOM file handling: reading, sorting, matching patients, and organizing."""

import os
import numpy as np
import pydicom as dicom

from patientIDextractor import Extract
from save_folder_tree import folder_tree
from clean_text import clean_text


class dicom_handler:
    """Read, match, and sort DICOM files into a structured folder hierarchy."""

    def unsortedlist(self, src):
        """Walk the source directory and collect all file paths.

        Parameters
        ----------
        src : str
            Root directory to scan.

        Returns
        -------
        list of str
            Paths to all files found under src.
        """
        unsortedList = []
        for root, dirs, files in os.walk(src):
            for file in files:
                unsortedList.append(os.path.join(root, file))

        print(f"{len(unsortedList)} files found.")
        return unsortedList

    def search_patid_in_dir(self, directory, matched_patient_id):
        """Search for a patient ID folder within the source directory.

        Parameters
        ----------
        directory : str
            Parent directory to search in.
        matched_patient_id : str
            Patient ID to look for.

        Returns
        -------
        list of str or None
            File paths within the matched folder, or None if not found.
        """
        if matched_patient_id in os.listdir(directory):
            return self.unsortedlist(os.path.join(directory, matched_patient_id))
        return None

    def patient_names_extractor(self, patientIDlist, patientnameslist, dst):
        """Match patient IDs to names from the database CSV.

        Parameters
        ----------
        patientIDlist : list of str
            Patient IDs extracted from directory names.
        patientnameslist : list of list
            Rows from the patient names CSV.
        dst : str
            Destination directory (unused, kept for interface compatibility).

        Returns
        -------
        np.ndarray
            Matched patient name/ID entries, shape (N, num_csv_columns).
        list
            List of all patient IDs processed.
        """
        matches = []
        id_list = []

        for i in range(len(patientIDlist)):
            pid = patientIDlist[i]
            str_match = [s for s in patientnameslist if pid in s]

            if str_match:
                print(f"Match found for {pid}: {str_match}")
                matches.append(str_match)
            id_list.append(pid)

        print(f"Total matches: {len(matches)}")
        num_cols = len(matches[0][0]) if matches else 5
        return np.reshape(matches, (len(matches), num_cols)), id_list

    def str_match_handler(self, patientIDlist, patientnameslist, dst):
        """Run patient name matching and return results.

        Parameters
        ----------
        patientIDlist : list of str
        patientnameslist : list of list
        dst : str

        Returns
        -------
        np.ndarray or list
            Matched entries, or empty list if no matches found.
        """
        str_match, _ = self.patient_names_extractor(patientIDlist, patientnameslist, dst)

        if str_match.size > 0:
            return str_match
        else:
            print("No matches found — check for duplicate entries in the CSV.")
            return []

    def patient_info_segregator(self, dicom_loc):
        """Extract patient and study metadata from a single DICOM file.

        Parameters
        ----------
        dicom_loc : str
            Path to the DICOM file.

        Returns
        -------
        tuple
            (dataset, path, filename, patientID, studyDate,
             studyDescription, seriesDescription)
        """
        ds = dicom.read_file(dicom_loc, force=True)

        patientID = clean_text(ds.get("PatientID", "NA"))
        studyDate = clean_text(ds.get("StudyDate", "NA"))
        studyDescription = clean_text(ds.get("StudyDescription", "NA"))
        seriesDescription = clean_text(ds.get("SeriesDescription", "NA"))
        modality = ds.get("Modality", "NA")
        instanceNumber = str(ds.get("InstanceNumber", "0"))

        fileName = f"{modality}.{seriesDescription}.{instanceNumber}.dcm"

        return ds, dicom_loc, fileName, patientID, studyDate, studyDescription, seriesDescription

    def dicom(self, unsortedList, patientIDlist, patientID_dir, patientnameslist, src, dst):
        """Main sorting pipeline: match patients and organize DICOM files.

        Parameters
        ----------
        unsortedList : list of str
            All file paths from the source directory.
        patientIDlist : list of str
            Patient IDs found in the source.
        patientID_dir : list of str
            Full paths to patient ID directories.
        patientnameslist : list of list
            Patient name database rows.
        src : str
            Source root directory.
        dst : str
            Destination output directory.
        """
        folder_patient_name_list = self.str_match_handler(patientIDlist, patientnameslist, dst)

        for patient_name in folder_patient_name_list:
            folder_patient_name = patient_name[0] + "_" + patient_name[1] + patient_name[2]
            matched_patient_id = patient_name[4]
            print(f"Processing: {folder_patient_name} (ID: {matched_patient_id})")

            matched_directory = self.search_patid_in_dir(src, matched_patient_id)

            if matched_directory is not None:
                for dicom_loc in matched_directory:
                    ds, dicom_loc, fileName, patientID, studyDate, studyDescription, seriesDescription = (
                        self.patient_info_segregator(dicom_loc)
                    )
                    folder_tree(
                        ds, dst, folder_patient_name, dicom_loc, fileName,
                        patientID, studyDate, studyDescription, seriesDescription,
                    )
            else:
                for dicom_loc in unsortedList:
                    ds, dicom_loc, fileName, patientID, studyDate, studyDescription, seriesDescription = (
                        self.patient_info_segregator(dicom_loc)
                    )
                    print(f"No matched directory for {matched_patient_id}, processing from unsorted list.")

        print("Done.")
