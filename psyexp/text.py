#!/usr/bin/env python3

"""
I'm starting with simple timed text presentation in the interpreter. It
will be expanded, of course, but for now I'm just getting the feel for
what's going on.
"""

# import time
from psyexp.experiment import Trial
import pyglet as pyg


class TextTrial(Trial):
    def __init__(self, stimulus, **kwargs):
        super().__init__(**kwargs)
        # Change the font sometime.
        self.stimulus = pyg.text.Label(stimulus,
                                       font_name="Courier New",
                                       font_size=36,
                                       anchor_x="center", anchor_y="center")
        self.duration = kwargs.get("duration", 10000)/1000.0

    def go(self):
        # self.time()
        self.stimulus.draw()
