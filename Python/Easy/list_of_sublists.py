#Author: Claudia (@cloelou)
def list_of_sublists(x, y, z):
    #(int, int, str/num) -> list
    #Return a list of x sublists. Each sublist contains only the z argument repeated
    #y times.
    #
    #>>> matrix(2, 1, "edabit")
    #[["edabit"], ["edabit"]]
    #>>> matrix(3, 2, 0)
    #[[0, 0], [0, 0], [0, 0]]
    lst = []
    for j in range(x):
	sublst = []
	for i in range(y):
	    sublst.append(z)
	lst.append(sublst)
    return lst
