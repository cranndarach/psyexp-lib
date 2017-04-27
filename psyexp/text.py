#!/usr/bin/env python3

"""
I'm starting with simple timed text presentation in the interpreter. It
will be expanded, of course, but for now I'm just getting the feel for
what's going on.
"""

import pyglet as pyg
import warnings
import math
import time


def present_text(stimulus, **kwargs):
    window = kwargs["window"]
    allowed_keys = kwargs.get("allowed_keys", [])
    keys_pressed = []
    duration = kwargs.get("duration", math.inf)/1000
    if duration <= 0.01:
        warnings.warn("Very short duration specified." +
                      " Did you remember to use seconds?")

    # I don't love defining the event handler for each trial, but I think
    # it's the only way to constrain it to this scope
    @window.event
    def on_key_press(key, modifiers):
        if key in allowed_keys:
            keys_pressed.append(key)

    stim = pyg.text.Label(stimulus,
                          font_name="Courier New",
                          font_size=36,
                          anchor_x="center",
                          anchor_y="center")
    start_time = time.clock()
    stim.draw()
    while time.clock()-start_time <= duration:
        # Any better way to signal a press to the loop?
        if keys_pressed:
            break
    end_time = time.clock()
    # Convert to msec
    start_time = round(start_time, 3) * 1000
    end_time = round(end_time, 3) * 1000
    rt = end_time - start_time
    response = keys_pressed[0]
    trial_results = {"StartTime": start_time,
                     "EndTime": end_time,
                     "RT": rt,
                     "Response": response}
    return trial_results
