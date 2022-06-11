def frequency(lst, search_term):
    """Return frequency of term in lst.
    
        >>> frequency([1, 4, 3, 4, 4], 4)
        3
        
        >>> frequency([1, 4, 3], 7)
        0
    """

    loop_dict = {}
    for num in lst:
        loop_dict[f'{num}'] = 0
    for num in lst:
        loop_dict[f'{num}'] += 1
    

    for num in lst:
        if num == search_term:
            return loop_dict[f'{num}']
    return 0