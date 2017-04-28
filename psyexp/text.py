#!/usr/bin/env python3

"""
I'm starting with simple timed text presentation in the interpreter. It
will be expanded, of course, but for now I'm just getting the feel for
what's going on.
"""

import pyglet as pyg
import psyexp.experiment as expt
import random as rd
import warnings
import math
import time


def present_text(stimulus, **kwargs):
    window = kwargs["window"]
    stim_label = kwargs["stim_label"]
    allowed_keys = kwargs.get("allowed_keys", [])
    norm_allowed_keys = [k.lower() for k in allowed_keys]
    keys_pressed = []
    duration = kwargs.get("duration", math.inf)
    additional_fields = kwargs.get("additional_fields", {})
    jitter = kwargs.get("jitter", False)
    if jitter:
        jitter_mean = kwargs["jitter_mean"]
        jitter_sd = kwargs["jitter_sd"]
        iti = rd.gauss(jitter_mean, jitter_sd)
    else:
        iti = kwargs.get("iti", 0)/1000.0
        warnings.warn("No ITI given. Defaulting to 0.") if not iti else None
    # if jitter:
    #     pyg.clock.schedule_once(window.clear, rd.gauss(jitter_mean, jitter_sd))
    # else:
    #     pyg.clock.schedule_once(window.clear, iti)
    if duration >= 100:
        warnings.warn("Very long duration specified.\
                      Did you remember to use seconds?")
    stim = pyg.text.Label(stimulus[stim_label],
                          font_name="Courier New",
                          font_size=36,
                          x=window.width//2,
                          y=window.height//2,
                          anchor_x="center",
                          anchor_y="center")

    start_time = time.clock()
    stim.draw()
    # If this is handled synchronously, it shouldn't do the rest until it
    # times out or receives a key press.
    pyg.clock.schedule_once(expt.timeout, delay=duration, **kwargs)

    @window.event
    def on_key_press(key, modifiers):
        print(key)
        norm_key = pyg.window.key.symbol_string(key).lower()
        if norm_key in norm_allowed_keys:
            keys_pressed.append(norm_key)
            pyg.clock.unschedule(expt.timeout)
            # expt.end_trial(stimulus, start_time, end_time,
            #                key_pressed=keys_pressed[0])

    @window.event
    def on_draw():
        window.clear()
        stim.draw()

    end_time = time.clock()
    # Convert to msec
    start_time = round(start_time, 3) * 1000
    end_time = round(end_time, 3) * 1000
    # If rt wasn't defined by timing out, define it now.
    response = keys_pressed[0] if keys_pressed else "None"
    rt = end_time - start_time if (response != "None") else math.inf
    trial_results = {"StartTime": start_time,
                     "EndTime": end_time,
                     "RT": rt,
                     "Response": response}
    trial_data = {**stimulus, **trial_results, **additional_fields}
    pyg.clock.schedule_once(expt.wait_iti, delay=iti, **kwargs)
    # expt.wait_iti(**kwargs)
    return trial_data
