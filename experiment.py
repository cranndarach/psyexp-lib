#!/usr/bin/env python3

"""
General task script.
"""

import time
import random as rd


def task(trials, **kwargs):
    jitter = kwargs.get("jitter", None)
    jitter_mean = jitter["mean"] if jitter else None
    jitter_sd = jitter["sd"] if jitter else None
    iti = rd.gauss(jitter_mean, jitter_sd)/1000.0 if jitter\
        else kwargs.get("iti")/1000.0
    [[trial, time.sleep(iti)] for trial in trials]
