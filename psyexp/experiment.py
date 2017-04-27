#!/usr/bin/env python3

"""
General task script.
"""

import time
import random as rd
import pyglet as pyg
import csv
# import pandas as pd
# import numpy as np


class Experiment(pyg.app.EventLoop):
    def __init__(self, **kwargs):
        super().__init__()
        # fill in formatting stuff later
        self.win = pyg.window.Window()
        self.allowed_keys = []

    def on_draw(self):
        self.win.clear()
        self.draw()

    def on_key_press(self, symbol, modifiers):
        key = pyg.key.symbol_string(symbol)
        if key in self.allowed_keys:
            self.endtime = time.clock()
            self.response = key
            self.rt = self.endtime - self.starttime
            self.win.clear()


# Okay so instead of a class per trial type, instead there should be a
# trial runner, and the parameters and everything can be passed around.
# Then we can skip most steps and just pass the stim list to this.
def generate_task(stimlist, trial_runner, **kwargs):
    gen = (trial_runner(stimulus=stim, **kwargs) for stim in stimlist)
    return gen, kwargs


def run_task(*args, **kwargs):
    # If they pass a template, use it, and if they pass
    # a sequence of named arguments instead, use them:
    exp = kwargs["experiment"]
    stimuli = kwargs["stimuli"]
    template = kwargs.get("template", kwargs)
    # If they pass the generator as the first argument, use it;
    # if they pass it as a named argument or as part of the
    # template, use that:
    gen = args[0] if args else template["gen"]
    jitter = template.get("jitter", False)
    if jitter:
        jitter_mean = template["jitter_mean"]
        jitter_sd = template["jitter_sd"]
    else:
        iti = template.get("iti", 0)/1000.0
        print("Warning: no ITI given. Defaulting to 0.") if not iti else None
    data = []
    for stim in stimuli:
        # I don't think this try...except format is needed, but I'm
        # leaving it until it can be tested.
        # try:
        exp.starttime = time.clock()
        next(gen)
        trial_results = {"StartTime": exp.starttime,
                        "EndTime": exp.endtime,
                        "RT": exp.rt,
                        "Response": exp.response}
        trial_data = {**stimulus, **trial_results}
        data.append(trial_data)
        if jitter:
            time.sleep(rd.gauss(jitter_mean, jitter_sd))
        else:
            time.sleep(iti)
        # except StopIteration:
        #     break
    return data
