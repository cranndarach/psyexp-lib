# Python Psych Experiment library

Psychology experiment library, similar idea to [PsychoPy](http://www.psychopy.org/).

**Please note that this is very much a work in progress!** You won't find it
on PyPI yet, because it is not even ready for a full release (though I do plan
to host it there as soon as it is released). Likewise, I do plan on documenting
everything once the project is a little more stable, which I hope will be very soon.

You're welcome to try it out now, especially if you want to contribute early on.
But if you're looking for a full-blown library to use for actual experiment development,
you might want to put this one on the back burner and come back later.

## Why will this be useful?

* It's good to have multiple options.
* Uses Python 3, which is standard now. This could especially make it easier
for anyone who is just now learning Python for the purpose of programming experiments.
* Style focus is more on functional programming than object-oriented. Functional
programming has some benefits, e.g.:
    * Efficiency and readability of code (fewer lines for the same outcome)
    * Easier to maintain control (minimizes the consequences on existing objects)
    * And to match the experiment logic a little better (write your program as a
    sequence of steps)
* This library has/will have a function for just about every step, which should
also make it easier for beginners. 
* I plan to follow PEP8/"Pythonic" style as much as possible, so that the source
will be easy enough to navigate and the project will welcome contributions.

## License information

This project is copyright (c) 2017 Rachael J. Steiner and licensed under the terms
of the BSD 3-Clause license.
