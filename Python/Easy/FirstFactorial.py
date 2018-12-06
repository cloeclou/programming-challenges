#Author: Claudia (@cloeclou)
def FirstFactorial(num): 
    #(int) -> int
    #Returns the factorial of num
    #Precondition: numbers being passed should be integers
    #
    #>>>FirstFactorial(4)
    #24
    #>>>FirstFactorial(8)
    #40320
    
    factorial = 1
    for n in range(1,num+1):
        factorial = factorial*n
    return factorial
    
