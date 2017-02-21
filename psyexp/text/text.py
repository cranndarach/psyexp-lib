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
import pyglet as pyg


class TextTrial(Trial):

    def __init__(self, stimulus, **kwargs):
        super().__init__(**kwargs)
        self.stimulus = pyg.text.Label(stimulus)
