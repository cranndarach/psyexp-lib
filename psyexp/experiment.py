#!/usr/bin/env python3

"""
General task script.
"""

import time
import random as rd
import pyglet as pyg
# from utils import decorator


class Experiment(pyg.EventLoop):
    def __init__(self, **kwargs):
        super().__init__()
        # fill in formatting stuff later
        self.win = pyg.window.Window()
        self.task_gen = None
        self.jitter_mean = None
        self.jitter_sd = None
        self.iti = None
        self.allowed_keys = []

    # def add_trial(self, name, trial, **kwargs):
    #     # kwargs might include the row from the stimulus df?
    #     # trial = Trial(stimulus, **kwargs)
    #     self.__setattr__(name, trial)

    def sequencer(self, member_names, **template):
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
        for member in member_names:
            # fill in
            self.current_trial = self.__getattr__(member)
            self.starttime = time.clock()
            self.current_trial.go()  # ?
            self.win.clear()
            time.sleep(self.iti)
        # Clean up:
        self.sequence_cleanup()

    def sequence_cleanup(self):
        # Add to this
        self.current_trial = None
        self.allowed_keys = []
        self.iti = self.jitter = self.jitter_sd = self.jitter_mean = None

    def on_draw(self):
        self.win.clear()
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


class Trial:
    # I think the question rn is does this actually do anything? Or is it
    # just a template? My only thought it that it will be best to keep it
    # to handle things with importing list properties.

    def __init__(self, stimulus, **kwargs):
        # I'm not sure if it makes more sense to have this and
        # make subclasses for types of trials, or to nuke trial
        # and have Stimulus classes, or what. But rather than
        # require people to make stims with pyglet there needs
        # to be something better. Maybe they'll all have a stimulus
        # attribute, but subclasses will handle it differently,
        # and then if people want to expand on that they can use pyg.
        pass
        # self.stimulus = stimulus

    def go(self):
        # Virtual ish
        pass
        # No pun intended

    # def handle_keypress(self, key):
    #     # A task or something can call Trial.handle_keypress()
    #     if key in self.allowed_keys:
    #         self.endtime = time.clock()
    #         self.response = key
    #         self.rt = self.endtime - self.starttime

    # def time(self):
    #     # Subclasses with run() methods should call Trial.time() to
    #     # start the clock if timing is important.
    #     self.starttime = time.clock()


def task_generator(trials, **kwargs):
    return {"gen": (trial.go() for trial in trials),
            "template": kwargs
            }


# @decorator
def run_task(gen, template):
    # allowed_keys = template.get("allowed_keys", [])
    # ^ mute the warning for now. But probably do some partial
    # to assign it to the experiment.
    jitter = template.get("jitter", False)
    if jitter:
        jitter_mean = template["jitter_mean"]
        jitter_sd = template["jitter_sd"]
    else:
        iti = template.get("iti", 0)/1000.0
        print("Warning: no ITI given. Defaulting to 0.") if not iti else None
    while True:
        try:
            next(gen)
            if jitter:
                time.sleep(rd.gauss(jitter_mean, jitter_sd))
            else:
                time.sleep(iti)
        except StopIteration:
            break

# They probably need better names. A task is a sequence of trials
# and an experiment is a sequence of tasks: so run_task means to
# run trials, and run_experiment would mean to run the tasks.
# run_task = run_generator
# run_sequence = run_generator
