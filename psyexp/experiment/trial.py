#!/usr/bin/env python3

"""
I'm giving in and going OO.
"""

# import pyglet as pyg
import time


class Trial:

    def __init__(self, **kwargs):
        self.allowed_keys = kwargs.get("allowed_keys", [])
        self.starttime = time.clock()
        # self.task = task

    def handle_keypress(self, key):
        # A task or something can call Trial.handle_keypress()
        if key in self.allowed_keys:
            self.endtime = time.clock()
            self.response = key
            self.rt = self.endtime - self.starttime
