def friend_date(a, b):
    """Given two friends, do they have any hobbies in common?

    - a: friend #1, a tuple of (name, age, list-of-hobbies)
    - b: same, for friend #2

    Returns True if they have any hobbies in common, False is not.

        >>> elmo = ('Elmo', 5, ['hugging', 'being nice'])
        >>> sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
        >>> gandalf = ('Gandalf', 10000, ['waving wands', 'chess'])

        >>> friend_date(elmo, sauron)
        False

        >>> friend_date(sauron, gandalf)
        True
    """

    
    a_hobbies = []
    b_hobbies = []
    
    for hobby in a[2]:
        a_hobbies.append(hobby)
    for hobby in b[2]:
        b_hobbies.append(hobby)

    a_hobbies = set(a_hobbies)
    b_hobbies = set(b_hobbies)
    combo_hobbies = a_hobbies & b_hobbies

    if (len(combo_hobbies) == 0):
        return False
    else: 
        return True
    
