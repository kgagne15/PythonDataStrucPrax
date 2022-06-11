def truncate(phrase, n):
    """Return truncated-at-n-chars version of  phrase.
    
    If the phrase is longer than, or the same size as, n make sure it ends with '...' and is no
    longer than n.
    
        >>> truncate("Hello World", 6)
        'Hel...'
        
        >>> truncate("Problem solving is the best!", 10)
        'Problem...'
        
        >>> truncate("Yo", 100)
        'Yo'
        
    The smallest legal value of n is 3; if less, return a message:
    
        >>> truncate('Cool', 1)
        'Truncation must be at least 3 characters.'

        >>> truncate("Woah", 4)
        'W...'

        >>> truncate("Woah", 3)
        '...'
    """

    if n >= 3:
        leftover = n - 3
        if leftover > len(phrase):
            return phrase
        elif leftover == 0:
            return '...'
        else:
            new_phrase = []
            for n in range(leftover):
                new_phrase.append(phrase[n])
            for n in range(3):
                new_phrase.append('.')
            new_phrase = ''.join(new_phrase)
            return new_phrase
    else:
        return 'Truncation must be at least 3 characters.'
    