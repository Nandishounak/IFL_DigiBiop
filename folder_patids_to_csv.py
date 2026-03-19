"""Export patient IDs from a directory listing to a CSV file."""

import os
import csv


def pat_id_to_csv(path, output_csv):
    """List subdirectories in path and write them to a CSV file.

    Parameters
    ----------
    path : str
        Directory whose subdirectories represent patient IDs.
    output_csv : str
        Path to the output CSV file.

    Returns
    -------
    list of str
        The list of directory entries.
    """
    my_list = os.listdir(path)
    print(f"Found {len(my_list)} entries in {path}")

    with open(output_csv, "w", newline="") as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(my_list)

    return my_list
