def is_odd_string(word):
    """Is the sum of the character-positions odd?

    Word is a simple word of uppercase/lowercase letters without punctuation.

    For each character, find it's "character position" ("a"=1, "b"=2, etc).
    Return True/False, depending on whether sum of those numbers is odd.

    For example, these sum to 1, which is odd:
    
        >>> is_odd_string('a')
        True

        >>> is_odd_string('A')
        True

    These sum to 4, which is not odd:
    
        >>> is_odd_string('aaaa')
        False

        >>> is_odd_string('AAaa')
        False

    Longer example:
    
        >>> is_odd_string('amazing')
        True
    """
    sum = 0
    loop_dict = {}
    alpha = 'abcdefghijklmnopqrstuvwxyz'

    for letter in alpha:
        idx = alpha.index(letter) + 1
        # print(letter, idx)
        loop_dict[letter] = idx


    for letter in word:
        value = loop_dict[letter.lower()]
        sum = sum + value

    if sum % 2 == 0:
        return False
    else:
        return True

    # Hint: you may find the ord() function useful here