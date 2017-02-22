#!/usr/bin/env python3

"""
General task script.
"""

import time
import random as rd
import pyglet as pyg
# from psyexp.utils.errors import MissingItiError


class Experiment(pyg.EventLoop):
    def __init__(self, **kwargs):
        super().__init__()
        # fill in formatting stuff later
        self.win = pyg.window.Window()
        self.jitter_mean = None
        self.jitter_sd = None
        self.iti = None

    def sequence(self, members, **template):
        # Members are trials. Contain stimuli & trial-specific info.
        # I think it could just be pyglet objects, though they should
        # probably be wrapped for the sake of keeping things simple.
        # Template is the task structure. Contains ITI, allowed keys, etc.
        # I think it could just be some kwargs (hence the ** for now).
        #
        # Set it up:
        self.allowed_keys = template.get("allowed_keys", [])
        jitter = template.get("jitter", False)
        if jitter:
            self.jitter_mean = template["jitter_mean"]
            self.jitter_sd = template["jitter_sd"]
        else:
            self.iti = template.get("iti", 0)/1000.0
            print("Warning: no ITI specified. Defaulting to 0.") if not \
                self.iti else None
        # Do the things:
        for trial in members:
            self.current_trial = trial
            # etc.
        # Clean up:
        self.sequence_cleanup()

    def sequence_cleanup(self):
        # Add to this
        self.allowed_keys = []

    def on_draw(self):
        self.clear()

    def on_key_press(self, symbol, modifiers):
        key = pyg.key.symbol_string(symbol)
        if key in self.allowed_keys:
            self.endtime = time.clock()
            self.response = key
            self.rt = self.endtime - self.starttime
            # self.current_trial.stop()? self.sequence.continue-sort-of(?)

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
        # self.allowed_keys = kwargs.get("allowed_keys", [])
        # self.task = task
        pass

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
