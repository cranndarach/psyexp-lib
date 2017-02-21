#!/usr/bin/env python3

"""
Misc. utilities.
"""

import time
import curses


def handle_buttonpress(allowed_keys, timeout):
    # Start up curses
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    curses.keypad(True)
    # idk
    win.nodelay(1)
    starttime = endtime = time.clock()
    while endtime < starttime+timeout:
        key_pressed = win.getkey()
        endtime = time.clock()
        if key_pressed in allowed_keys:
            response = key_pressed
            break
    rt = endtime - starttime
    # Call in the exorcist
    curses.nocbreak()
    curses.keypad(False)
    curses.echo()
    curses.endwin()
    return (response, rt)
