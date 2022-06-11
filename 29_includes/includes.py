def includes(collection, sought, start=None):
    """Is sought in collection, starting at index start?

    Return True/False if sought is in the given collection:
    - lists/strings/sets/tuples: returns True/False if sought present
    - dictionaries: return True/False if *value* of sought in dictionary

    If string/list/tuple and `start` is provided, starts searching only at that
    index. This `start` is ignored for sets/dictionaries, since they aren't
    ordered.

        >>> includes([1, 2, 3], 1)
        True

        >>> includes([1, 2, 3], 1, 2)
        False

        >>> includes("hello", "o")
        True

        >>> includes(('Elmo', 5, 'red'), 'red', 1)
        True

        >>> includes({1, 2, 3}, 1)
        True

        >>> includes({1, 2, 3}, 1, 3)  # "start" ignored for sets!
        True

        >>> includes({"apple": "red", "berry": "blue"}, "blue")
        True
    """

    if isinstance(collection, list) or isinstance(collection, str) or isinstance(collection, tuple):
        if start == None:
            for item in collection:
                if item == sought:
                    return True
            return False
        else:
            for item in collection:
                if item == sought and collection.index(item) >= start:
                    return True
            return False
    else: 
        if isinstance(collection, set):
            for item in collection:
                if item == sought:
                    return True
            return False
        elif isinstance(collection, dict):
            for k,v in collection.items():
                if v == sought:
                    return True
            return False