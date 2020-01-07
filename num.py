

def num_check(password, num_numbers=1):
    '''
    (str, int) -> bool 
    Contains a number of number characters. 
    Have it optionally take a num_numbers arg
    >>> check_num('Woops')
    False
    >>> check_num('Woops33', 2)
    True
    >>> check_num('Woops33', 6)
    False
    '''
    num_count = 0 
    for each in password:
        if each.isnumeric():  # isnum() does not exist- check docs
            # rather than return, increment the num_count
            # return True
            num_count += 1
    if num_count >= num_numbers:
        return True
    else:
        return False
    # The above if/else can be reduced to one liner
