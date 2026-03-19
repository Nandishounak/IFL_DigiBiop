"""
DICOM Image Segregation Pipeline

Sorts DICOM files by modality and scan type for each patient, then
renames patient folders using a master CSV of patient names and IDs.

Usage:
    python main.py --source /path/to/dicom/root \
                   --destination /path/to/output \
                   --patient-db /path/to/patient_names.csv
"""

import argparse
from patientIDextractor import pat_id_extractor, Extract
from csv_reader import csv_read
from dicom_handler import dicom_handler


def parse_args():
    parser = argparse.ArgumentParser(
        description="Sort DICOM files by modality/scan type and assign patient names."
    )
    parser.add_argument(
        "--source",
        required=True,
        help="Root directory containing patient DICOM folders.",
    )
    parser.add_argument(
        "--destination",
        required=True,
        help="Output directory for the sorted folder structure.",
    )
    parser.add_argument(
        "--patient-db",
        required=True,
        help="Path to the CSV file mapping patient IDs to names.",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    # Extract patient IDs from source directory
    patientIDlist, patientID_dir = pat_id_extractor(args.source)

    # Read patient name database
    patientnameslist = csv_read(args.patient_db)

    assert type(patientnameslist) == type(patientIDlist)

    print(f"Patient IDs in source folder: {patientIDlist}")
    print(f"Patient IDs in database: {Extract(patientnameslist)}")
    print(f"  {len(Extract(patientnameslist))} IDs in database")

    # Sort and organize DICOM files
    handler = dicom_handler()
    unsortedList = handler.unsortedlist(args.source)
    handler.dicom(
        unsortedList,
        patientIDlist,
        patientID_dir,
        patientnameslist,
        args.source,
        args.destination,
    )


if __name__ == "__main__":
    main()
