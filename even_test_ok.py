def is_even(num):
    '''
    >>> is_even(2)
    True
    >>> is_even(3)
    False
    '''
    if num % 2 == 0:
        return True
    else:
        return False

# if __name__ == '__main__':
#     import doctest
#     doctest.testmod()