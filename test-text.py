#!/usr/bin/env python3

import psyexp.experiment as expt
from psyexp import text
from psyexp import utils

wordlist = utils.load_list("test-list.csv", shuffle=True)

e = expt.Experiment()

e.allowed_keys = ["Z", "/"]
ldt_data = expt.run_task(expt.generate_task(text.generate_trials(wordlist,
                         "Stimulus", jitter=True, jitter_mean=400,
                                                                 jitter_sd=50)))

e.run()

utils.save_data(ldt_data, "test-data.csv")
