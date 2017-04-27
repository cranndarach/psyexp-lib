#!/usr/bin/env python3

"""
General task script.
"""

import time
import random as rd
import pyglet as pyg
import csv
# import math


def generate_task(stimlist, trial_runner, **kwargs):
    gen = (trial_runner(stimulus=stim, **kwargs) for stim in stimlist)
    return gen


def run_task(task, **kwargs):
    gen = task
    window = kwargs["window"]
    additional_fields = kwargs.get("additional_fields", {})
    data = []
    jitter = kwargs.get("jitter", False)
    if jitter:
        jitter_mean = kwargs["jitter_mean"]
        jitter_sd = kwargs["jitter_sd"]
    else:
        iti = kwargs.get("iti", 0)/1000.0
        print("Warning: no ITI given. Defaulting to 0.") if not iti else None

    # for stim in stimuli:
    for trial in gen:
        trial_results = next(gen)
        if trial_results:
            trial_data = {**stim, **trial_results, **additional_fields}
            data.append(trial_data)
        window.clear()
        if jitter:
            time.sleep(rd.gauss(jitter_mean, jitter_sd))
        else:
            time.sleep(iti)
    return data


def run_experiment(*sequence, **kwargs):
    window = kwargs["window"]

    @window.event
    def on_draw():
        win.clear()
        draw()

    # So make a generator that runs each task
    tasks = (run_task(t, **kwargs) for t in sequence)
    nested_data = [task_data for task_data in tasks]
    # Flatten the data list
    data = [line for task in nested_data for line in task]
    return data
