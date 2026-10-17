"""
File helpers.

Reads and writes the JSON data files, and appends error messages to
logs.txt. Errors are not handled here on purpose: the caller decides
how to react (see the load_* and save_* functions in main.py).
"""

import json


def read_file(file_path):
    """Read a JSON file and return its contents (a list of dicts here)."""

    with open(file_path, "r" , encoding = "utf-8") as file:
        return json.load(file)


def update_file(file_path , write_data):
    """Overwrite a JSON file with write_data, formatted for readability."""

    with open(file_path, "w" , encoding = "utf-8") as file:
        json.dump(write_data , file ,indent = 4)


def log_error(error_message):
    """Append one error message to logs.txt, one message per line."""

    # "a" (append) keeps earlier log entries instead of overwriting them.
    with open("logs.txt" , "a" ,encoding ="utf-8") as file:
        file.write(error_message + "\n")