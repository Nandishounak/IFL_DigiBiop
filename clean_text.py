"""Sanitize DICOM metadata strings for use as filenames and folder names."""


def clean_text(string):
    """Replace filesystem-unsafe characters with underscores and lowercase.

    Parameters
    ----------
    string : str
        Raw DICOM metadata string.

    Returns
    -------
    str
        Cleaned, lowercase string safe for file/folder names.
    """
    forbidden_symbols = ["*", ".", ",", "\"", "\\", "/", "|", "[", "]", ":", ";", " "]
    for symbol in forbidden_symbols:
        string = string.replace(symbol, "_")
    return string.lower()
