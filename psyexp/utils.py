#!/usr/bin/env python3

"""
Misc. utilities. Mostly wrappers for pandas functions.
"""

# import pandas as pd
import csv
import random as rd


def load_list(filepath, **kwargs):
    stims = []
    sep = kwargs.get("sep", ",")
    # df = pd.read_csv(filepath, sep)
    # df.set_index(stimulus_col, inplace=True)
    with open(filepath) as stimcsv:
        reader = csv.DictReader(stimcsv, delim=sep)
        for row in reader:
            stims.append(row)
    if kwargs.get("shuffle", False):
        # df = df.sample(frac=1)
        rd.shuffle(stims)
    else:
        None
    return stims


def save_data(data, filepath):
    # data.to_csv(filepath)
    with open(filepath, "w") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        for row in data:
            writer.writerow(row)
    return True
