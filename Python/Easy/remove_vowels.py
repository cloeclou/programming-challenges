#Author: Claudia (@cloeclou)
def remove_vowels(txt):
    #(str) -> str
    # Removes all values from the txt string and returns the resulting string.
    #
    #>>> remove_vowels('I have never seen a thin person drinking Diet Coke.')
    #' hv nvr sn  thn prsn drnkng Dt Ck.'
    #>>> remove_vowels('Happy Thanksgiving to all')
    #'Hppy Thnksgvng t ll'
    vowels = 'aeiouAEIOU'
    list_letters = list(txt)
    for i in range(len(list_letters)-1,-1,-1):
        if list_letters[i] in vowels:
            list_letters.pop(i)
    final = ''.join(list_letters)
    return final

