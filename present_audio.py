#!/usr/bin/env python3

"""
Work in progress. Goal is to write it somewhat functionally.
"""

# import wave
import simpleaudio as sa
import time
# from sys import stdout
import random as rd


def load_stims(filenames, shuffle=False):
    rd.shuffle(filenames) if shuffle else None
    return [sa.WaveObject.from_wave_file(fp) for fp in filenames]


def audio_trial(waveobject, **kwargs):
    jitter = kwargs.get("jitter", None)
    jitter_mean = jitter["mean"] if jitter else None
    jitter_sd = jitter["sd"] if jitter else None
    iti = rd.gauss(jitter_mean, jitter_sd)/1000.0 if jitter\
        else kwargs.get("iti")/1000.0
    # stim = waveobject.play()
    # stim.wait_done()
    waveobject.play().wait_done()
    print("next")
    time.sleep(iti)

prefix = "/home/rachael/Documents/School/kiloperf/stimuli/"\
    + "wordsbyword/words{}.wav"
stims = load_stims([prefix.format("ache"), prefix.format("beast"),
                    prefix.format("ail")])
# time.sleep(3)
print("loaded stimuli")
[audio_trial(stim, iti=1000) for stim in stims]
