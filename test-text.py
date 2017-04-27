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
ldt_trials = text.generate_trials(wordlist, jitter_mean=400, jitter_sd=50)
ldt_task = expt.generate_task(ldt_trials)
ldt_data = expt.run_task(ldt_task)
# ldt_data = expt.run_task(expt.generate_task(text.generate_trials(wordlist,
#                                             "Stimulus", jitter=True,
#                                             jitter_mean=400, jitter_sd=50)))

e.run()

utils.save_data(ldt_data, "test-data.csv")
