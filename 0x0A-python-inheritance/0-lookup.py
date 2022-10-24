#!/usr/bin/python3
"""
Contains definition of the function lookup
"""


def lookup(obj):
    """Returns the list of available attributes and methods of an object

    Args:
        obj (any): object whose attributes and methods are to be returned

    """

    return dir(obj)
