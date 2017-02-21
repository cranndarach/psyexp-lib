#!/usr/bin/env python3

from psyexp.text import text
from psyexp.experiment import experiment as exp

stims = ["hello", "world", "colorless", "green", "ideas", "sleep", "furiously"]
trials = [text.text_trial(stim, 3000) for stim in stims]
exp.task(trials, jitter={"mean": 500, "sd": 100})
