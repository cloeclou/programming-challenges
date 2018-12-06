#Author: Claudia (@cloeclou)
def FirstReverse(string): 
    #(str) -> (str)
    #Returns the string str in reverse order.
    #
    #>>>FirstReverse('I Love Code')
    #'edoC evoL I'
    #>>>FirstReverse('numerically')
    #'yllaciremun'

    reverse = ''
    for i in range(len(string)):
        reverse = reverse + string[len(string)-1-i]
    return reverse
    

