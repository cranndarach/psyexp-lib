#!/usr/bin/env python3

import random as rd
from psyexp.text.text import TextTrial
from psyexp.experiment.experiment import Task, Experiment
# from psyexp.experiment import experiment as exp

stims = ["hello", "world", "colorless", "green", "ideas", "sleep", "furiously"]
rd.shuffle(stims)
EXP = Experiment()
task = Task(EXP, iti=500)
task.trials = [TextTrial(stim, duration=3000, allowed_keys=["Z", "/"])
               for stim in stims]
EXP.tasks.append(task)
EXP.run()
