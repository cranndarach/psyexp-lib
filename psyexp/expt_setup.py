#!/usr/bin/env python3

"""
Loading lists, setting up data output.
"""

import pandas as pd


def load_list(filepath, **kwargs):
    """
    Effectively a wrapper for pandas.read_csv()
    """
    return pd.read_csv(filepath, **kwargs)


# def create_index(df, data_col, **kwargs):
    # indices = kwargs.get("indices", range(1, len()))
