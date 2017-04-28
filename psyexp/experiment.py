#!/usr/bin/env python3

"""
General experiment script.
"""

# import time
import random as rd
import pyglet as pyg
import csv
# import math


def generate_task(stimlist, trial_runner, **kwargs):
    gen = (trial_runner(stimulus=stim, **kwargs) for stim in stimlist)
    return gen


def run_task(task, **kwargs):
    gen = task
    data = [trial for trial in gen]
    return data


def run_experiment(*sequence, **kwargs):
    window = kwargs["window"]
    tasks = (run_task(t, **kwargs) for t in sequence)
    nested_data = [task for task in tasks]
    # Flatten the data list
    data = [line for task in nested_data for line in task]
    # window.close()
    return data


# Not sure how to handle this
def start():
    pyg.app.run()


def end_trial(stimulus, start_time, end_time, key_pressed=None):
    start_time = int(round(start_time, 3) * 1000)
    end_time = int(round(end_time, 3) * 1000)
    # If rt wasn't defined by timing out, define it now.
    rt = end_time - start_time if not rt else rt
    response = key_pressed if key_pressed else "None"
    trial_results = {"StartTime": start_time,
                     "EndTime": end_time,
                     "RT": rt,
                     "Response": response}
    trial_data = {**stimulus, **trial_results}
    return trial_data


def timeout(delay, **kwargs):
    window = kwargs["window"]
    window.clear()
    return


def wait_iti(delay, **kwargs):
    window = kwargs["window"]
    window.clear()
