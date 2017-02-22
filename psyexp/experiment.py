#!/usr/bin/env python3

"""
General task script.
"""

import time
import random as rd
import pyglet as pyg
# from psyexp.utils.errors import MissingItiError


class Experiment(pyg.window.Window):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # fill in formatting stuff later
        self.tasks = []
        self.task = None

    def run_task(self, task):
        self.task = task
        self.task.run()

    def on_draw(self):
        self.clear()

    def on_key_press(self, symbol, modifiers):
        key = pyg.key.symbol_string(symbol)
        self.task.handle_keypress(key)

    def run(self):
        try:
            [self.run_task(task) for task in self.tasks]
            pyg.app.run()
        except:
            pyg.app.exit()
            raise


class Task:
    def __init__(self, experiment, **kwargs):
        self.jitter = kwargs.get("jitter", None)
        if self.jitter:
            self.jitter_mean = self.jitter["mean"]
            self.jitter_sd = self.jitter["sd"]
        else:
            self.iti = kwargs.get("iti", 0)/1000.0
            if not self.iti:
                print("Warning: no ITI specified. Defaulting to 0.")
            # except KeyError:
            #     # Maybe make it a warning sometime.
            #     raise MissingItiError("Please specify an inter-trial " +
            #                           "interval (ITI) or jitter.")
        self.experiment = experiment
        self.done = False
        self.trials = []
        self.trial = None

    def jitter_iti(self):
        return rd.gauss(self.jitter_mean, self.jitter_sd)/1000.0

    def handle_keypress(self, key):
        self.trial.handle_keypress(key)

    def run_trial(self, trial):
        self.trial = trial
        self.trial.start()
        # self.experiment.clear()
        # self.trial = None
        # time.sleep(self.iti)

    def run(self):
        [[self.run_trial(trial), time.sleep(self.iti)] for trial in self.trials]
        self.done = True


class Trial:

    def __init__(self, **kwargs):
        self.allowed_keys = kwargs.get("allowed_keys", [])
        # self.task = task

    def handle_keypress(self, key):
        # A task or something can call Trial.handle_keypress()
        if key in self.allowed_keys:
            self.endtime = time.clock()
            self.response = key
            self.rt = self.endtime - self.starttime

    def time(self):
        # Subclasses with run() methods should call Trial.time() to
        # start the clock if timing is important.
        self.starttime = time.clock()
