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
    stim_key = kwargs["stim_key"]
    allowed_keys = kwargs.get("allowed_keys", [])
    norm_allowed_keys = [k.lower() for k in allowed_keys]
    keys_pressed = []
    duration = kwargs.get("duration", math.inf)
    if duration >= 100:
        warnings.warn("Very long duration specified.\
                      Did you remember to use seconds?")
    stim = pyg.text.Label(stimulus[stim_key],
                          font_name="Courier New",
                          font_size=36,
                          anchor_x="center",
                          anchor_y="center")

    # I don't love defining the event handler for each trial, but I think
    # it's the only way to constrain it to this scope.
    # But figure out if it can at least be partly separated out, because
    # it shouldn't be rewritten for every type of trial that requires a
    # key press.
    @window.event
    def on_key_press(key, modifiers):
        print(key)
        norm_key = pyg.key.symbol_string(key).lower()
        if norm_key in norm_allowed_keys:
            keys_pressed.append(norm_key)

    @window.event
    def on_draw():
        win.clear()
        draw()

    start_time = time.clock()
    stim.draw()
    while time.clock()-start_time <= duration:
        # Any better way to signal a press to the loop?
        if keys_pressed:
            break
    else:
        rt = math.inf
    end_time = time.clock()
    # Convert to msec
    start_time = round(start_time, 3) * 1000
    end_time = round(end_time, 3) * 1000
    # If rt wasn't defined by timing out, define it now.
    rt = end_time - start_time if not rt else rt
    response = keys_pressed[0] if keys_pressed else "None"
    trial_results = {"StartTime": start_time,
                     "EndTime": end_time,
                     "RT": rt,
                     "Response": response}
    trial_data = {**stimulus, **trial_results}
    return trial_data
