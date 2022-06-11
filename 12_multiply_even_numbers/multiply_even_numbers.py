def multiply_even_numbers(nums):
    """Multiply the even numbers.
    
        >>> multiply_even_numbers([2, 3, 4, 5, 6])
        48
        
        >>> multiply_even_numbers([3, 4, 5])
        4
        
    If there are no even numbers, return 1.
    
        >>> multiply_even_numbers([1, 3, 5])
        1
    """
    even_nums = [num for num in nums if num % 2 == 0]
    if len(even_nums) != 0:
        product = 1
        for num in even_nums:
            product = product * num
        return product
    else:
        return 1

#helpful link: https://www.geeksforgeeks.org/python-multiply-numbers-list-3-different-ways/