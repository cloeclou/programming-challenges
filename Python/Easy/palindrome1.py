#Author: Claudia (@cloeclou)
#This is the first out of 3 different algorithms to check for palindromes.
def palindrome1(sen):
    # (str) -> boolean
    # Returns True if sen is a boolean or booleanic sentence, returns False if not.
    # Precondition: Do not include punctuation (periods, exclamation marks, etc)
    #
    #>>> palindrome1('Hannah')
    #True
    #>>> palindrome1('dentist')
    #False
    #>>> palindrome1('Noel sees Leon')
    #True

    sen_compare = sen.lower() #eliminates effect of capital letters
    sen_inv=sen_compare[::-1]
    return sen_compare==sen_inv
