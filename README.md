# IFL_DigiBiop
This script is prepared in order to segregate the dicom images. The script performs the following tasks-
1. Sorting the DICOM files based on modalities and type of scans for a particular patient ID. These patient file are contained in separate 'year of scan folder'.
2. The final task is assigning the names of the patient in the patient folder, after taking the data from the master csv file containing the patient names with their corresponding IDs.
3. The Patient ID with the names .csv file should contain the patient IDS starting with "000" in  order to get them matched with the script. Since the default folder created by the PACS during the data acquisition has the PACS ID as a ten-digit number, this step needs to be ensured for the code to run.
4. The csv file which stores the patient names and their corresponding IDs must ensure that there are no duplicate entries.
5. It is to be noted that some patient names may have special alphabets like ü, ö, ä, etc. which must be checked in a csv file reader before feeding the file into the script to avoid garbage values in the folder names.
