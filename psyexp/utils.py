#!/usr/bin/env python3

"""
Misc. utilities. Mostly wrappers for pandas functions.
"""

# import time
# import pyglet as pyg
import pandas as pd


def load_list(filepath, stimulus_col, **kwargs):
    df = pd.read_csv(filepath, kwargs)
    df.set_index(stimulus_col, inplace=True)
    if kwargs.get("shuffle", False):
        df.sample(frac=1)
    else:
        None
    return df


def save_data(data, filepath):
    data.to_csv(filepath)
    return True
