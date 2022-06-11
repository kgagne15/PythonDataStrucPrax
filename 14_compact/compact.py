def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    new_lst = []
    for item in lst:
        new_lst.append(item)
    
    true_list = [item for item in new_lst if bool(item) == True]
    return true_list

#helpful link: https://www.w3schools.com/python/python_booleans.asp