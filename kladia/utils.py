"""
This module contains utility functions for the project.
author: @jocerfranquiz
date: 2022-12-31
version: 0.0.1
"""

import sys
import functools


def memoize(func):
    """Decorator that caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned (not
    reevaluated).

    Source: https://wiki.python.org/moin/PythonDecoratorLibrary#Memoize
    """
    cache = func.cache = {}

    @functools.wraps(func)
    def memoizer(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return memoizer


@memoize
def dict_order(d):
    if not isinstance(d, dict):
        raise TypeError('dict_order function only accepts dictionaries')
    if not d:  # empty dictionary
        return -1
    max_order = -1
    for value in d.values():
        if isinstance(value, dict):
            order = dict_order(value)
            if order > max_order:
                max_order = order
            else:
                continue
        elif value is None:
            continue
    return max_order + 1


def get_size(obj, seen=None):
    """Recursively finds size of objects
Source: https://goshippo.com/blog/measure-real-size-any-python-object/ The
get_size function has a time complexity of O(n), where n is the number of nodes and links in the graph. This is
because the function traverses the entire graph, visiting each node and link once.

The space complexity of the get_size function is also O(n), because the function stores a list of seen objects in the
seen parameter, which can grow up to the size of the graph.

In general, the time and space complexity of the get_size function is determined by the size of the graph,
rather than the number of attributes associated with the nodes or links. This is because the function only needs to
visit each node and link once, regardless of how many attributes they have.

    Args:
        obj (object): Object to get size of
        seen (set, optional): Set of objects already seen. Defaults to None.

    Returns:
        int: Size of object in bytes

    """
    size = sys.getsizeof(obj)
    if seen is None:
        seen = set()
    obj_id = id(obj)
    if obj_id in seen:
        return 0
    # Important mark as seen *before* entering recursion to gracefully handle
    # self-referential objects
    seen.add(obj_id)
    if isinstance(obj, dict):
        size += sum([get_size(v, seen) for v in obj.values()])
        size += sum([get_size(k, seen) for k in obj.keys()])
    elif hasattr(obj, '__dict__'):
        size += get_size(obj.__dict__, seen)
    elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
        size += sum([get_size(i, seen) for i in obj])
    return size


if __name__ == "__main__":

    # Test get_size function
    print(get_size({}))  # 64 bytes
    print(get_size({0: {}}))  # 320 bytes
    print(get_size({0: {0: {}}}))  # 552 bytes
    print(get_size({0: {0: {0: {}}}}))  # 784 bytes
    print(get_size(None))  # 16 bytes
    print(get_size({0: None}))  # 272 bytes
    print(get_size({0: {0: None}}))  # 504 bytes
    print(get_size({0: {0: {0: None}}}))  # 736 bytes

    _none = {0: {0: {1: None, 2: None}, 1: {0: None, 2: None}, 2: {0: None, 1: None, 3: None}, 3: {2: None}}}
    print(get_size(_none))
    _empty = {0: {0: {1: {}, 2: {}}, 1: {0: {}, 2: {}}, 2: {0: {}, 1: {}, 3: {}}, 3: {2: {}}}}
    print(get_size(_empty))

    # Test dict_order function
    print(dict_order({}))  # -1
    print(dict_order({0: None}))  # 0
    print(dict_order({0: {0: None}}))  # 1
    print(dict_order({0: {0: {0: None}}}))  # 2

    print(dict_order(_none))  # 2
