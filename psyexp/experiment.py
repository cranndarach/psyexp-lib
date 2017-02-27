#!/usr/bin/env python3

"""
General task script.
"""

import time
import random as rd
import pyglet as pyg
import pandas as pd
# from utils import decorator


class Experiment(pyg.EventLoop):
    def __init__(self, **kwargs):
        super().__init__()
        # fill in formatting stuff later
        self.win = pyg.window.Window()
        self.allowed_keys = []

    def on_draw(self):
        self.win.clear()
        # Consider how to do this.
        self.current_trial.draw()

    def on_key_press(self, symbol, modifiers):
        key = pyg.key.symbol_string(symbol)
        if key in self.allowed_keys:
            self.endtime = time.clock()
            self.response = key
            self.rt = self.endtime - self.starttime
            # Need some sort of means of handling data output.
            # Could use some sort of functools method (e.g., a partial?)
            # to pass the response, RT, and any relevant properties of
            # the stimulus/task to a global data logging utility, which
            # can then get the rest of its arguments from the task or trial?
            # handle_trial_data(handle_all_data, self.rt, self.response)
            self.win.clear()
            # Should this indeed be a member, or should it refer to some
            # external var? Hard to imagine the latter without making people
            # code it themselves, but the former is not very fp.
            next(self.task_gen)


class Trial:
    def __init__(self, stimulus, df, stimulus_col, **kwargs):
        self.stimulus = stimulus
        self.stimcol = stimulus_col
        self.row = df.loc[stimulus]

    def go(self):
        # Virtual ish
        pass
        # No pun intended

    # def time(self):
    #     # Subclasses with run() methods should call Trial.time() to
    #     # start the clock if timing is important.
    #     self.starttime = time.clock()


def generate_task(trials, **kwargs):
    # Add a list of rows to the template to be passed on:
    kwargs["row"] = [trial.row for trial in trials]
    # Plop the generator and any arguments into a dict.
    return {"gen": (trial.go() for trial in trials),
            "template": kwargs
            }


def run_task(*args, **kwargs):
    # If they pass a template, use it, and if they pass
    # a series of named arguments instead, use them.
    exp = kwargs["experiment"]
    rows = kwargs["rows"]
    template = kwargs.get("template", kwargs)
    # If they pass the generator as the first argument, use it;
    # if they pass it as a named argument or as part of the
    # template, use that.
    gen = args[0] if args else template["gen"]
    jitter = template.get("jitter", False)
    if jitter:
        jitter_mean = template["jitter_mean"]
        jitter_sd = template["jitter_sd"]
    else:
        iti = template.get("iti", 0)/1000.0
        print("Warning: no ITI given. Defaulting to 0.") if not iti else None
    # while True:
    colnames = rows[0].axes
    data_to_start = [[] for _ in range(len(colnames))]
    data = pd.DataFrame.from_dict(zip(colnames, data_to_start))
    for row in rows:
        try:
            exp.starttime = time.clock()
            next(gen)
            trial_data = pd.Series(data=[exp.starttime, exp.endtime, exp.rt,
                                         exp.response],
                                   index=["StartTime", "EndTime", "RT",
                                          "Response"])
            data.append(trial_data)
            if jitter:
                time.sleep(rd.gauss(jitter_mean, jitter_sd))
            else:
                time.sleep(iti)
        except StopIteration:
            break
    # Do something to output data
    return data
