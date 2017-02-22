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
