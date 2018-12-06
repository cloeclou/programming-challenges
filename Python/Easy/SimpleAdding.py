# Author: Claudia (@cloeclou)
def SimpleAdding(num): 
    # (int) -> int
    # Returns the addition of numbers 1 to num
    #
    #>>>SimpleAdding(5)
    #15
    #>>>SimpleAdding(-7)
    #0
    return sum(range(num+1))

