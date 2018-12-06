# Author: Claudia (@cloeclou)
def LetterChanges(string): 
    # (str) -> str
    # Substitutes each letter in the string with the letter following it in the alphabet
    # (and cycles back to the beginning after Z). If the output is a vowel, the vowel is
    # capitalized.
    #
    #>>>LetterChanges('hello! how are you?')
    #'Ifmmp! Ipx bsf zpv?'
    #>>>LetterChanges('Can you give me my book back?')
    #'DbO zpv hjwf nf nz cppl cbdl?'
    #
    a = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    b = 'bcdEfghIjklmnOpqrstUvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZA'
    changed = ''
    for i in range(len(string)):
        if string[i] in a:
            changed = changed + b[a.index(string[i])]
        else:
            changed = changed + string[i]
    return changed

    



