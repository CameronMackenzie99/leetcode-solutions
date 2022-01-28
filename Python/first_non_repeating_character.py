"""Different implementations of first_non_repeating_char with different time and space complexities"""



def first_non_repeating_char(string):
    """Given a string of lowercase english letters, returns the first non-repeating character in the string. If none, returns "_".

    :param string: str
    :return: str

    >>> first_non_repeating_char("aaabcccdeeef")
    'b'
    >>> first_non_repeating_char("abcbad")
    'c'
    >>> first_non_repeating_char("abcabcabc")
    '_'
    """
    # (O)n^2 - nested double for loop so O(n*n). Less memory usage as count is not stored for each iteration
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

    """Given a string of lowercase english letters, returns the first non-repeating character in the string. 

    :param string: str
    :return: str

    >>> first_non_repeating_char_2("aaabcccdeeef")
    'b'
    >>> first_non_repeating_char_2("abcbad")
    'c'
    >>> first_non_repeating_char_2("abcabcabc")
    '_'
    """
    # (O)n^2 - nested double for loop so O(n*n). Lower complexity floor Ω(n) than first_non_repeating_char as inner for loop has break condition for any count over one.
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

def first_non_repeating_char_3(string):
    """Given a string of lowercase english letters, returns the first non-repeating character in the string. 

    :param string: str
    :return: str

    >>> first_non_repeating_char_3("aaabcccdeeef")
    'b'
    >>> first_non_repeating_char_3("abcbad")
    'c'
    >>> first_non_repeating_char_3("abcabcabc")
    '_'
    """
    # O(2n) ~= O(n) as upper bound of complexity is looping through the string twice.
    charstring = {}

    for i in range(len(string)):
        if string[i] not in charstring:
            charstring[string[i]] = 1
        else:
            charstring[string[i]] += 1

    for char in string:
        if charstring[char] == 1:
            return char
    return "_" 

if __name__ == "__main__":
    import doctest
    doctest.testmod()