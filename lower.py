import doctest

def check_lwr(password, num_lower=2):
    '''
    (str, int)->bool
    Contains min 2 lowercase chars.
    Optionally takes a num_lower arg
    >>> check_lwr('Password6')
    True
    >>> check_lwr('PASS6')
    False
    >>> check_lwr('PASS6', 0)
    True
    >>> check_lwr('abcdefg', 6)
    True
    >>> check_lwr('PSaSwORD7', 3)
    False
    '''
    lwr_count = 0
    for each in password:
        if each.islower():
            lwr_count += 1
    return lwr_count >= num_lower



if __name__ == "__main__":
    doctest.testmod()