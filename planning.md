# Psyexp-lib planning

>Stream of consciousness about oop/fp. Note to future self: I have a migraine rn.

Okay so I want to limit the object-orientedness while keeping it user-friendly
and mostly contained (so that most of what people will have to write will be
part of the library). So naturally there will be *some* classes (e.g., Experiment),
but maybe I can make everything else methods on the class instead of classes
that have to become associated somehow with the experiment class.

Association is important for pyglet apps (and probably just about any GUI lib),
because of events etc.

This honestly might even work reasonably well with Tkinter—thinking about how
I organized LifeTracker. But idk.

Bc I'm thinking about the ideal sort of flow, and it keeps coming back to
`Experiment.add_task()` types of things.

```python
e = Experiment()
e.add_task("mytask", iti=500, allowed_keys=["Z", "/"])
e.add_trial() # to a task? or something?
```

Starting to think maybe making "tasks" into more like "task templates."  
So you could have like "run this sequence of trials with this task style."

## More FP

Okay so now that I read the HOWTO on fp in Python, I'm getting a slightly better
feel for how to go about this.

I still might write relevant classes, but the flow can be more functional.

thoughts:

```python
task1_list = load_list("path/to/task1list.csv", shuffle=True)
task2_list = load_list("path/to/task2list.csv", shuffle=True)

TASK_ALLOWED_KEYS = ["Z", "/"]

exp = Experiment(...)

task1_schema = text.generate_trials(task1_list, "Stimuli")
task1 = generate_task(task1_schema)

task2_schema = text.generate_trials(task2_list, "Stimuli")
task2 = generate_task(task2_schema)

exp.allowed_keys = TASK_ALLOWED_KEYS
task1_data = run_task(task1)
task2_data = run_task(task2)

exp.run()

save_data(task1_data, "path/to/data")
save_data(task2_data, "path/to/data2")
```

If you wanted to be really fancy:

```python
# [start with loading lists, etc.]

exp.allowed_keys = TASK_ALLOWED_KEYS
task1_data = run_task(generate_task(text.generate_trials(task1_list, "Stimuli")))

exp.run()

save_data(task1_data, "path/to/data")
```
