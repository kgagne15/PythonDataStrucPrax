def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    loop_dict = {}
    vowels = 'aeiou'
    for letter in phrase:
        new_letter = letter.lower()
        for vowel in vowels:
            if new_letter == vowel:
                loop_dict[new_letter] = 0
        
    for letter in phrase:
        new_letter = letter.lower()
        for vowel in vowels:
            if new_letter == vowel:
                loop_dict[new_letter] += 1
    return loop_dict