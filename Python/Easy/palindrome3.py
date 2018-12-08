#Author: Claudia (@cloeclou)
#This is the third out of 3 different algorithms to check for palindromes.
def palindrome3(sen):
    # (str) -> boolean
    # Returns True if sen is a boolean or booleanic sentence, returns False if not.
    # Precondition: Do not include punctuation (periods, exclamation marks, etc)
    #
    #>>> palindrome3('Hannah')
    #True
    #>>> palindrome3('dentist')
    #False
    #>>> palindrome3('Noel sees Leon')
    #True

    sen_compare = sen.lower() #eliminates effect of capital letters
    result = 1
    i = 0
    while i<=(len(sen_compare)//2):
        result = result*(sen_compare[i]==sen_compare[-1-i]) #compares characters pair-wise
        if result == 0:
            return False
        i = i+1
            
    return True
