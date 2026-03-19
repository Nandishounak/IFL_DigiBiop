"""Extract patient IDs from a directory structure."""

import os
import glob
from operator import itemgetter


def Extract(lst):
    """Extract the last element from each sublist (typically the patient ID).

    Parameters
    ----------
    lst : list of list
        Rows from the patient names CSV.

    Returns
    -------
    list
        Last element of each row.
    """
    return [item[-1] for item in lst]


def pat_id_extractor(path):
    """Extract patient IDs from subdirectory names.

    Parameters
    ----------
    path : str
        Root directory containing one subdirectory per patient ID.

    Returns
    -------
    pat_id_list : list of str
        Patient IDs (subdirectory names).
    store_dir_patids : list of str
        Full paths to each patient subdirectory.
    """
    pat_id_list = []

    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            pat_id_list.append(entry)

    print(f"Found {len(pat_id_list)} patient IDs in source path")
    store_dir_patids = glob.glob(os.path.join(path, "*"))

    return pat_id_list, store_dir_patids


def flatten(lst):
    """Flatten a list of lists into a single list."""
    return [item for sublist in lst for item in sublist]
