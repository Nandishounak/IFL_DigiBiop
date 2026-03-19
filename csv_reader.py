"""Read the patient names CSV database."""

import csv


def csv_read(path):
    """Read a CSV file and return all rows as a list of lists.

    Uses ISO-8859-1 encoding to handle special characters (e.g., ü, ö, ä).

    Parameters
    ----------
    path : str
        Path to the CSV file.

    Returns
    -------
    list of list
        Each inner list is a row from the CSV.
    """
    rows = []
    with open(path, encoding="ISO-8859-1", newline="") as csvfile:
        reader = csv.reader(csvfile, delimiter=",", quotechar="|")
        for row in reader:
            rows.append(row)

    print(f"Read {len(rows)} rows from {path}")
    return rows
