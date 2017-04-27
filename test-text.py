#!/usr/bin/env python3

import psyexp.experiment as expt
from psyexp import text
from psyexp import utils
# import sys

wordlist = utils.load_list("test-list.csv", sep=",", shuffle=True)
# print(wordlist)
# sys.exit(0)

e = expt.Experiment()
e.allowed_keys = ["Z", "/"]

params = {"jitter": True, "jitter_mean": 400, "jitter_sd": 50}

# ldt_trials = text.generate_trials(wordlist, jitter_mean=400, jitter_sd=50)
# ldt_task = expt.generate_task(ldt_trials)
ldt_task = expt.generate_task(wordlist, text.present_text, **params)
ldt_data = expt.run_task(ldt_task)

e.run()

utils.save_data(ldt_data, "test-data.csv")
