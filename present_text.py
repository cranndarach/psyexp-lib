#!/usr/bin/env python3

"""
I'm starting with simple timed text presentation in the interpreter. It
will be expanded, of course, but for now I'm just getting the feel for
what's going on.
"""

import time
from sys import stdout

# Actually, time.sleep() exists
# starttime = endtime = time.clock()
# counter = 0
# while endtime < starttime+0.5:
#     counter += 1
#     endtime = time.clock()
#
# print(starttime, endtime, endtime-starttime, counter)


def present_stimulus(stimulus, duration):
    duration /= 1000.0
    stdout.write("\r{}".format(stimulus))
    stdout.flush()
    time.sleep(duration)


def experiment(stimuli, trial_dur, iti):
    iti /= 1000.0
    overwrite = " "*max([len(stim) for stim in stimuli])
    for stim in stimuli:
        present_stimulus(stim, trial_dur)
        stdout.write("\r{}".format(overwrite))
        stdout.flush()
        time.sleep(iti)
    stdout.write("\n")

stims = ["hello", "world", "colorless", "green", "ideas", "sleep", "furiously"]
experiment(stims, 500, 250)
