import sys

"""
This module contains utility functions for the project.
"""


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

    print(100 - get_size(_none) / get_size(_empty) * 100)

    _str = '{0: {0: {1: {}, 2: {}}, 1: {0: {}, 2: {}}, 2: {0: {}, 1: {}, 3: {}}, 3: {2: {}}}}'
    print(get_size(_str))  # 130 bytes