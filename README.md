# IFL_DigiBiop

DICOM image segregation pipeline that sorts medical imaging files by modality and scan type, then assigns patient names from a master database.

## What it does

1. **Scans** a root directory containing patient DICOM folders (organized by year of scan).
2. **Matches** patient IDs from the folder names against a master CSV database containing patient names and IDs.
3. **Sorts** DICOM files into a structured hierarchy: `PatientName / PatientID / StudyDate / StudyDescription / SeriesDescription /`.
4. **Renames** folders with patient names from the database.

## Usage

```bash
pip install -r requirements.txt

python main.py \
    --source /path/to/dicom/root \
    --destination /path/to/output \
    --patient-db /path/to/patient_names.csv
```

### Arguments

| Argument | Description |
|---|---|
| `--source` | Root directory containing patient DICOM folders |
| `--destination` | Output directory for the sorted folder structure |
| `--patient-db` | Path to CSV mapping patient IDs to names |

## Patient database CSV format

The CSV file should contain patient names and IDs with the following requirements:

- Patient IDs must start with `000` to match the 10-digit PACS ID format.
- No duplicate entries — duplicates will cause matching errors.
- Special characters (ü, ö, ä, etc.) should be verified with a CSV reader before use to avoid encoding issues. The script uses ISO-8859-1 encoding.

## Output structure

```
destination/
└── LastName_FirstName/
    └── PatientID/
        └── StudyDate/
            └── StudyDescription/
                └── SeriesDescription/
                    ├── MR.series_desc.1.dcm
                    ├── MR.series_desc.2.dcm
                    └── ...
```

## Project structure

| File | Description |
|---|---|
| `main.py` | Entry point — parses arguments and runs the pipeline |
| `dicom_handler.py` | Core DICOM reading, patient matching, and sorting logic |
| `patientIDextractor.py` | Extracts patient IDs from directory names |
| `csv_reader.py` | Reads the patient names CSV database |
| `clean_text.py` | Sanitizes DICOM metadata strings for safe filenames |
| `save_folder_tree.py` | Creates the nested output folder structure |
| `folder_patids_to_csv.py` | Utility to export directory patient IDs to CSV |

## Dependencies

- Python 3.7+
- [pydicom](https://pydicom.github.io/)
- numpy
