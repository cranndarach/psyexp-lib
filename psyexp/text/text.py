#!/usr/bin/env python3

"""
I'm starting with simple timed text presentation in the interpreter. It
will be expanded, of course, but for now I'm just getting the feel for
what's going on.
"""

# import time
from psyexp.experiment.trial import Trial
import pyglet as pyg


class TextTrial(Trial):

    def __init__(self, stimulus, task, **kwargs):
        super().__init__(**kwargs)
        self.stimulus = pyg.text.Label(stimulus,
                                       font_name="Fira Mono Regular", size=36,
                                       anchor_x="center", anchor_y="center")
        self.duration = kwargs.get("duration", 10000)/1000.0
        self.task = task

    def start(self):
        self.time()
        self.stimulus.draw()
        # time.sleep(self.duration)
        # self.handle_keypress()

        # There's got to be a better way
        # @self.task.experiment.window.event
        # def on_draw():
        #     self.task.experiment.window.clear()
        #     self.stimulus.draw()

        @self.task.experiment.window.event
        def on_key_press(symbol):
            key_pressed = pyg.symbol_string(symbol)
            self.handle_keypress(key_pressed)
