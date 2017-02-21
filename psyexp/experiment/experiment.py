#!/usr/bin/env python3

"""
General task script.
"""

import time
# from sys import stdout
# import ncurses as nc
import random as rd
import pyglet as pyg


class Task:
    def __init__(self, trials, **kwargs):
        self.jitter = kwargs.get("jitter", None)
        self.jitter_mean = self.jitter["mean"] if self.jitter else None
        self.jitter_sd = self.jitter["sd"] if self.jitter else None
        self.iti = rd.gauss(self.jitter_mean, self.jitter_sd)/1000.0 if\
            self.jitter else kwargs.get("iti")/1000.0

    # Not done!!

# def task(trials, **kwargs):
#     jitter = kwargs.get("jitter", None)
#     jitter_mean = jitter["mean"] if jitter else None
#     jitter_sd = jitter["sd"] if jitter else None
#     iti = rd.gauss(jitter_mean, jitter_sd)/1000.0 if jitter\
#         else kwargs.get("iti")/1000.0
#     # win = nc.initscr()
#     # win.nodelay(1)
#     [[trial, time.sleep(iti)] for trial in trials]
#     # stdout.write("\n")
#     # In case it becomes important to think about synchrony:
#     return True
#
#
# def experiment(sequence):
#     win = pyg.window.Window()
#
#     @win.event
#     def on_draw():
#         win.clear()
#         [task for task in sequence]
#
#     # return?
#     pyg.app.run()
