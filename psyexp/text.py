#!/usr/bin/env python3

"""
I'm starting with simple timed text presentation in the interpreter. It
will be expanded, of course, but for now I'm just getting the feel for
what's going on.
"""

import pyglet as pyg


def present_text(stimulus, **kwargs):
    pyg.text.Label(stimulus,
                   font_name="Courier New",
                   font_size=36,
                   anchor_x="center",
                   anchor_y="center"
                   ).draw()
