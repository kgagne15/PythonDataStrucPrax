def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    total_phrase = []
    new_word = []
    split_phrase = phrase.split()
    for word in split_phrase:
        for letter in word:
            new_word.append(letter.lower())
        new_letter = new_word[0].upper()
        new_word.pop(0)
        new_word.insert(0, new_letter)
        new_word = ''.join(new_word)
        total_phrase.append(new_word)
        new_word = []
    return ' '.join(total_phrase)
    
        

