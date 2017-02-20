#!/usr/bin/env python3

"""
Jitter presentation of trials. Wrapper for random.gauss().
"""

import random as rd


def jitter(mean, sd):
    return rd.gauss(mean, sd)
