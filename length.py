# max is default function so should the module be renamed to something else also using (password) in the brackets will pass the current password that is in main.py e.g my function has def hashpass(password): < taken from main
def password_len(password, min_len=8):
    '''
    (str, int)->bool
    Length- at least 8. Make the function have a default of 8, but optionally take a min_len arg.
    >>> password_len('Password')
    True
    >>> password_len('Password', 12)
    False
    >>> password_len('Pass2', 3)
    True
    >>> password_len('Pass2')
    False
    '''
    return len(password) >= min_len
    # min_len !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"min_len" =string //!!!!!!!!!!!!!!!!!!!!!!!!! min_len = variable also password_len is a function not length of string or its index!
#if password_len >="min_len"