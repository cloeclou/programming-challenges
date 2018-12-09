#Author: Claudia (@cloeclou)
def is_isogram(txt):
    #(float,float,float) -> int
    #Returns the number of equal values from the input values. Output can be 0,2 or 3.
    #
    #>>> equal(1,2,3)
    #0
    #>>> equal(2,4,2)
    #2
    txt_lower=txt.lower() # neutralizes the effect of capital letters
    txt_set = set(txt_lower) # eliminate duplicates by obtaining the set of letters
    if len(set(txt_lower)) == len(txt_lower):
        return True
    else:
        return False

