#Author: Claudia (@cloeclou)
def is_valid_PIN(pin):
    #(str) -> boolean
    # Returns True is the input is a string consisting of 4 or 6 digits. 
    #
    #>>> is_valid_PIN('1234')
    #True
    #>>> is_valid_PIN('4g78')
    #False
    #>>> is_valid_PIN('79252')
    #False

    isnum=1
    if (len(pin)!=4 and len(pin)!=6):
	return False
    for i in range(len(pin)):
	isnum=isnum*pin[i].isnumeric()
    if isnum==0:
	return False
    else:
	return True
