#Author: Claudia (@cloeclou)
def anagram(str1, str2):
    #(str1, str2) -> boolean
    # Returns True if str1 and str2 are anagrams and False if not. Anagrams are 
    # words which contain the same letters but in different order. 
    #
    #>>> anagram('cristian', 'Cristina')
    #True
    #>>> anagram('Dave Barry', 'Ray Adverb')
    #True
    #>>> anagram('Nope', 'Note')
    #False
    #
    str1=str1.lower()
    str2=str2.lower()
    list1=sorted(str1)
    list2=sorted(str2)
    return list1==list2
