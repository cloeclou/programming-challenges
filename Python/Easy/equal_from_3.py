#Author: Claudia (@cloeclou)
def equal(a, b, c):
    #(float,float,float) -> int
    #Returns the number of equal values from the input values. Output can be 0,2 or 3.
    #
    #>>> equal(1,2,3)
    #0
    #>>> equal(2,4,2)
    #2

    if a==b and b==c and c==a:
        return 3
    elif a!=b and b!=c and c!=a:
        return 0
    else:
        return 2

