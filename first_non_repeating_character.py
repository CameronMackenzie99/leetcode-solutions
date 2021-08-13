"""Different implementations of first_non_repeating_char with different time and space complexities"""



def first_non_repeating_char(string):
    """ Function that outputs the first non-repeating character in a string of lowercase english letters. 
    >>> first_non_repeating_char("aaabcccdeeef")
    'b'
    >>> first_non_repeating_char("abcbad")
    'c'
    >>> first_non_repeating_char("abcabcabc")
    '_'
    >>> # no non-repeating characters so returns an underscore
    """
    charstring = list(str(string))

    for i in charstring:
        count = 0
        for j in charstring:
            if i == j:
                count += 1
        if count == 1:
            return i
    return "_"      

def first_non_repeating_char_2(string):

    """ Function that outputs the first non-repeating character in a string of lowercase english letters. 

    
    >>> first_non_repeating_char_2("aaabcccdeeef")
    'b'
    >>> first_non_repeating_char_2("abcbad")
    'c'
    >>> first_non_repeating_char_2("abcabcabc")
    '_'
    >>> # no non-repeating characters so returns an underscore
    """

    charstring = list(str(string))

    for i in range(len(charstring)):
        seen_duplicate= False
        for j in range(len(charstring)):
            if charstring[i] == charstring[j] and i != j:
                seen_duplicate = True
                break
        if seen_duplicate == False:
            return charstring[i]
    return "_" 

if __name__ == "__main__":
    import doctest
    doctest.testmod()