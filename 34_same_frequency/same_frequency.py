def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    loop_dict_one = {}
    for digit in str(num1):
        loop_dict_one[digit] = 0
    for digit in str(num1):
        loop_dict_one[digit] += 1


    loop_dict_two = {}
    for digit in str(num2):
        loop_dict_two[digit] = 0
    for digit in str(num2):
        loop_dict_two[digit] += 1
    

    for digit in str(num1):
        if loop_dict_one[digit] != loop_dict_two[digit]:
            return False
    return True

    #helpful link: https://www.knowprogram.com/python/python-iterate-over-digits-in-integer/