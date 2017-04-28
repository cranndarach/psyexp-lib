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
    # window = kwargs["window"]
    # additional_fields = kwargs.get("additional_fields", {})
    # data = []
    data = [next(gen) for _ in gen]
    # jitter = kwargs.get("jitter", False)
    # if jitter:
    #     jitter_mean = kwargs["jitter_mean"]
    #     jitter_sd = kwargs["jitter_sd"]
    # else:
    #     iti = kwargs.get("iti", 0)/1000.0
    #     print("Warning: no ITI given. Defaulting to 0.") if not iti else None

    # for trial in gen:
    # while True:
        # trial_results = next(gen)
        # print("trial completed")
        # if trial_results:
        #     trial_data = {**trial_results, **additional_fields}
        #     print(trial_data)
        #     data.append(trial_data)
        # window.clear()
        # if jitter:
        #     time.sleep(rd.gauss(jitter_mean, jitter_sd))
        # else:
        #     # time.sleep(iti)
        #     pyg.clock.schedule_once(continue, iti)
    return data


def run_experiment(*sequence, **kwargs):
    window = kwargs["window"]

    # @window.event
    # def on_draw():
    #     win.clear()
    #     draw()

    # So make a generator that runs each task
    tasks = (run_task(t, **kwargs) for t in sequence)
    nested_data = [next(tasks) for _ in tasks]
    # Flatten the data list
    data = [line for task in nested_data for line in task]
    window.close()
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


def timeout():
    window.clear()
    return


def wait_iti(**kwargs):
    window = kwargs["window"]
    jitter = kwargs.get("jitter", False)
    if jitter:
        jitter_mean = kwargs["jitter_mean"]
        jitter_sd = kwargs["jitter_sd"]
    else:
        iti = kwargs.get("iti", 0)/1000.0
        warnings.warn("No ITI given. Defaulting to 0.") if not iti else None
    if jitter:
        pyg.clock.schedule_once(window.clear, rd.gauss(jitter_mean, jitter_sd))
    else:
        pyg.clock.schedule_once(window.clear, iti)
