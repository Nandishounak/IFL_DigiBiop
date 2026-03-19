"""Create a nested folder structure and save sorted DICOM files."""

import os


def folder_tree(ds, dst, folder_patient_name, dicom_loc, fileName,
                patientID, studyDate, studyDescription, seriesDescription):
    """Save a DICOM file into a structured folder hierarchy.

    Creates the directory structure:
        dst / folder_patient_name / patientID / studyDate / studyDescription / seriesDescription /

    Parameters
    ----------
    ds : pydicom.Dataset
        The loaded DICOM dataset.
    dst : str
        Root destination directory.
    folder_patient_name : str
        Patient name string for the top-level folder.
    dicom_loc : str
        Original path to the DICOM file.
    fileName : str
        Standardized output filename (modality.series.instance.dcm).
    patientID : str
        Cleaned patient ID.
    studyDate : str
        Cleaned study date.
    studyDescription : str
        Cleaned study description.
    seriesDescription : str
        Cleaned series description.

    Returns
    -------
    None or result of ds.save_as()
        None if metadata fields are missing ("na"), otherwise the save result.
    """
    # Skip files with missing metadata
    if "na" in (patientID, studyDate, studyDescription, seriesDescription):
        return None

    # Build the nested directory path
    target_dir = os.path.join(
        dst, folder_patient_name, patientID,
        studyDate, studyDescription, seriesDescription,
    )
    os.makedirs(target_dir, exist_ok=True)

    print(f"Saving: {folder_patient_name} / {patientID} / {studyDate} / {studyDescription} / {seriesDescription}")
    return ds.save_as(os.path.join(target_dir, fileName))
