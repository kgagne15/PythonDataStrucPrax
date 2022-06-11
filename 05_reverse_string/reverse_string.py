def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    backwards_string = []
    for letter in reversed(phrase):
        backwards_string.append(letter)
    return ''.join(backwards_string)


#used this resource to loop backwards: https://python.plainenglish.io/how-to-loop-backwards-in-python-9724c25e8050