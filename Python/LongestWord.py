# Author: Claudia (@cloeclou)
def LongestWord(sen):
    #(str) -> str
    # Returns the longest word in sen, ignoring all punctuation.

    #>>>LongestWord(fun games)
    #games
    #>>>LongestWord(Hello! I am Jim)
    #Hello
    #>>>LongestWord(Are you in?????? No)
    #Are
    words = ['']
    j = 0
    for i in range(len(sen)):
        if sen[i] != ' ' and sen[i].isalpha():
            words[j] = words[j] + sen[i]
        elif sen[i] != ' ' and not sen[i].isalpha():
            words[j] = words[j]
        else:
            j = j+1;
            words.append('')
    lengths = []
    for i in range(len(words)):
        lengths.append(len(words[i]))
        
    return(words[lengths.index(max(lengths))])

