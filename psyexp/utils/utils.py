#!/usr/bin/env python3

"""
Misc. utilities.
"""

import time
# import ncurses as nc


def handle_buttonpress(allowed_keys, timeout, window_obj):
    starttime = endtime = time.clock()
    while endtime < starttime+timeout:
        key_pressed = window_obj.getkey()
        endtime = time.clock()
        if key_pressed in allowed_keys:
            response = key_pressed
            break
    rt = endtime - starttime
    return (response, rt)
