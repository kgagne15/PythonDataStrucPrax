def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    new_phrase = []
    for letter in phrase:
        to_swap_lower = to_swap.lower()
        if letter.lower() == to_swap or letter.upper() == to_swap:
            if letter.isupper() == True:
                new_phrase.append(letter.lower())
            else: 
                new_phrase.append(letter.upper())
        else:
            new_phrase.append(letter)
    new_phrase = ''.join(new_phrase)
    return new_phrase
