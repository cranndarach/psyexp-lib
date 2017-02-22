#!/usr/bin/env python3

"""
Errors specific to the package.
"""


class Error(Exception):
    """Base class for exceptions in this package."""
    pass


class MissingItiError(Error):
    """
    Exception raised when no intertrial interval is defined.
    """

    def __init__(self, message):
        self.message = message
