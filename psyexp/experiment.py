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
    # kwargs will probably contain something like iti or
    # jitter params. Just pass it along.
    return {"gen": (trial.go() for trial in trials),
            "template": kwargs
            }


def run_task(*args, **kwargs):
    # If they pass a template, use it, and if they pass
    # a series of named arguments instead, use them.
    template = args[1] if args else kwargs.get("template", kwargs)
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
    while True:
        try:
            next(gen)
            if jitter:
                time.sleep(rd.gauss(jitter_mean, jitter_sd))
            else:
                time.sleep(iti)
        except StopIteration:
            break
    # Do something to output data
    return True
