#Author: Claudia (@cloeclou)
#This is the second out of 3 different algorithms to check for palindromes.
def palindrome2(sen):
    # (str) -> boolean
    # Returns True if sen is a boolean or booleanic sentence, returns False if not.
    # Precondition: Do not include punctuation (periods, exclamation marks, etc)
    #
    #>>> palindrome2('Hannah')
    #True
    #>>> palindrome2('dentist')
    #False
    #>>> palindrome2('Noel sees Leon')
    #True

    sen_compare = sen.lower() #eliminates effect of capital letters
    if len(sen_compare)%2==0:
        sen_1st_half = sen_compare[0:int(len(sen_compare)/2)]
        sen_2nd_half = sen_compare[int(len(sen_compare)/2):len(sen_compare)]
    else:
        sen_1st_half = sen_compare[0:len(sen_compare)//2]
        sen_2nd_half = sen_compare[len(sen_compare)//2+1:len(sen_compare)]
    sen_2nd_half_inv=sen_2nd_half[::-1]
    return sen_1st_half==sen_2nd_half_inv
    
