def calculate(operation, a, b, make_int=False, message='The result is'):
    """Perform operation on a + b, ()possibly truncating) & returning w/msg.

    - operation: 'add', 'subtract', 'multiply', or 'divide'
    - a and b: values to operate on
    - make_int: (optional, defaults to False) if True, truncates to integer
    - message: (optional) message to use (if not provided, use 'The result is')

    Performs math operation (truncating if make_int), then returns as
    "[message] [result]"

        >>> calculate('add', 2.5, 4)
        'The result is 6.5'

        >>> calculate('subtract', 4, 1.5, make_int=True)
        'The result is 2'

        >>> calculate('multiply', 1.5, 2)
        'The result is 3.0'

        >>> calculate('divide', 10, 4, message='I got')
        'I got 2.5'

    If a valid operation isn't provided, return None.

        >>> calculate('foo', 2, 3)
        
    """
    if operation == 'add':
        if make_int == False:
            sum = a + b
            return message + ' ' + str(sum)
        else:
            sum = a + b
            sum = int(sum)
            return message + ' ' + str(sum)
    elif operation == 'subtract':
        if make_int == False:
            diff = a - b
            return message + ' ' + str(diff)
        else:
            diff = a - b
            diff = int(diff)
            return message + ' ' + str(diff)
    elif operation == 'multiply':
        if make_int == False:
            prod = a * b
            return message + ' ' + str(prod)
        else:
            prod = a * be
            prod = int(prod)
            return message + ' ' + str(prod)
    elif operation == 'divide':
        if make_int == False:
            res = a / b
            return message + ' ' + str(res)
        else:
            res = a / b
            res = int(res)
            return message + ' ' + str(res)
    else:
        return None


#helpful link: https://kodify.net/python/math/truncate-integers/