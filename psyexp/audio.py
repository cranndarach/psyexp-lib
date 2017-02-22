#!/usr/bin/env python3

"""
Present auditory stimuli. WIP.
"""

# import simpleaudio as sa
# import pygame as pyg
from psyexp.experiment import Trial
# import time
# import random as rd


class AudioTrial(Trial):
    def __init__(self, stimulus, **kwargs):
        super().__init__(**kwargs)
        # Assume stimulus is a pre-loaded pyg.media object
        self.stimulus = stimulus
        self.stimulus.play()


# def load_audio_stims(filenames, shuffle=False):
#     rd.shuffle(filenames) if shuffle else None
#     return [sa.WaveObject.from_wave_file(fp) for fp in filenames]
#
#
# def audio_trial(waveobject, **kwargs):
#     waveobject.play().wait_done()
#     print("next")
#
# prefix = "/home/rachael/Documents/School/kiloperf/stimuli/"\
#     + "wordsbyword/words{}.wav"
# stims = load_stims([prefix.format("ache"), prefix.format("beast"),
#                     prefix.format("ail")])
# print("loaded stimuli")
# [audio_trial(stim, iti=1000) for stim in stims]
