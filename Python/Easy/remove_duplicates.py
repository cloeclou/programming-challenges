#Author: Claudia (@cloelou)
def remove_duplicates(lst):
    #(list) -> list
    #Takes the list lst, removes all duplicate items and returns a new list
    #in the same sequential order as the old list (minus duplicates).
    #
    #>>> remove_duplicates(["John", "Taylor", "John"])
    #["John", "Taylor"]
    #>>> remove_duplicates([1, 0, 1, 0])
    #[1, 0]
    for i in range(len(lst)):
        for j in range(len(lst)-1,i,-1):
            if lst[i]==lst[j] and i!=j:
                lst.pop(j)
    return lst
