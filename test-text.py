#!/usr/bin/env python3

import pyglet as pyg
import psyexp.experiment as expt
from psyexp import text
from psyexp import utils
# import sys

wordlist = utils.load_list("test-list.csv", sep=",", shuffle=True)
window = pyg.window.Window()
params = {"jitter": True,
          "jitter_mean": 400,
          "jitter_sd": 50,
          "allowed_keys": ["Z", "slash"],
          "duration": 5,
          "window": window,
          "stim_key": "Stimulus"}

ldt_task = expt.generate_task(wordlist, text.present_text, **params)
# sys.exit(0)
ldt_data = expt.run_experiment(ldt_task, **params)

utils.save_data(ldt_data, "test-data.csv")
expt.start()
