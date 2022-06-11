def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    new_phrase = []
    for letter in phrase:
        new_phrase.append(letter)
    new_first = new_phrase[0].upper()
    new_phrase.pop(0)
    new_phrase.insert(0, new_first)
    new_phrase = ''.join(new_phrase)
    return new_phrase