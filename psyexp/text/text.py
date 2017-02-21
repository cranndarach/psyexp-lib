#!/usr/bin/env python3

"""
I'm starting with simple timed text presentation in the interpreter. It
will be expanded, of course, but for now I'm just getting the feel for
what's going on.
"""

# import time
# from sys import stdout
# import ncurses as nc
# from .utils import *
from psyexp.experiment.trial import Trial
# import pyglet as pyg


class TextTrial(Trial):

    def __init__(self, stimulus, **kwargs):
        super().__init__(**kwargs)


# def text_trial(stimulus, duration=3600000, **kwargs):
#     allowed_keys = kwargs.get("allowed_keys", [])
#     duration /= 1000.0
#     # stdout.write("\r{}".format(stimulus))
#     # stdout.flush()
#     response = ""
#     response, rt = utils.handle_buttonpress(allowed_keys, duration)
    # Overwrite the stimulus:
    # stdout.write("\r"+" "*len(stimulus))
    # stdout.flush()


# def experiment(stimuli, trial_dur, iti):
#     iti /= 1000.0
#     # overwrite = " "*max([len(stim) for stim in stimuli])
#     for stim in stimuli:
#         present_stimulus(stim, trial_dur)
#         # stdout.write("\r{}".format(overwrite))
#         # stdout.flush()
#         time.sleep(iti)
#     stdout.write("\n")
#
# stims = ["hello", "world", "colorless", "green", "ideas", "sleep",
#   "furiously"]
# experiment(stims, 500, 250)
