#Author: Claudia (@cloeclou)
def index_of_caps(word):
    #(str) -> list of integers
    #Returns the indices of capital letters in the string word.
    #
    #
    #>>>index_of_caps('iDEalLy')
    #[1,2,5]
    #>>>index_of_caps('STRIKE')
    #[0,1,2,3,4,5]

    caps = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    index_list = []
    for i in range(len(word)):
        if word[i] in caps:
            index_list.append(i)
    return index_list
