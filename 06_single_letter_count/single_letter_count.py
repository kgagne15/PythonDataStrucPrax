def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?
    
        >>> single_letter_count('Hello World', 'h')
        1
        
        >>> single_letter_count('Hello World', 'z')
        0
        
        >>> single_letter_count("Hello World", 'l')
        3
    """
    loop_dict = {}
    for el in word:
        case_el = el.lower()
        loop_dict[case_el] = 0
    for el in word:
        case_el = el.lower()
        loop_dict[case_el] += 1
    
    for k in loop_dict:
        if k == letter:
            return loop_dict[letter]
    return 0
