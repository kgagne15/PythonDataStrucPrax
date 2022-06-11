def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """

    loop_dict = {}
    for el in phrase:
        loop_dict[el] = 0
    for el in phrase:
        loop_dict[el] += 1

    print(loop_dict)