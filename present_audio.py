#!/usr/bin/env python3

"""
Work in progress. Goal is to write it somewhat functionally.
"""

import simpleaudio as sa
import time
import random as rd


def load_audio_stims(filenames, shuffle=False):
    rd.shuffle(filenames) if shuffle else None
    return [sa.WaveObject.from_wave_file(fp) for fp in filenames]


def audio_trial(waveobject, **kwargs):
    waveobject.play().wait_done()
    print("next")

prefix = "/home/rachael/Documents/School/kiloperf/stimuli/"\
    + "wordsbyword/words{}.wav"
stims = load_stims([prefix.format("ache"), prefix.format("beast"),
                    prefix.format("ail")])
print("loaded stimuli")
[audio_trial(stim, iti=1000) for stim in stims]
