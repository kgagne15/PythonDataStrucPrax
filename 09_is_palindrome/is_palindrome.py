def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    backwards_phrase = []
    lower_phrase = []
    for letter in reversed(phrase):
        low_case_letter = letter.lower()
        backwards_phrase.append(low_case_letter)
    
    backwards_phrase = ''.join(backwards_phrase)
    backwards_phrase = backwards_phrase.replace(' ', '')


    for letter in phrase:
        low_case_letter = letter.lower()
        lower_phrase.append(low_case_letter)
    
    lower_phrase = ''.join(lower_phrase)
    lower_phrase = lower_phrase.replace(' ', '')

    if backwards_phrase == lower_phrase:
        return True
    else:
        return False


#used the following resource to replace spaces: https://www.geeksforgeeks.org/python-remove-spaces-from-a-string/