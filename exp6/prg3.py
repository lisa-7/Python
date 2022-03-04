# experiment no 6 List
L = [1, 2, 3]
print(L)                                                                #[1, 2, 3]

#del element from list
del L[1]
print(L)                                                                #[1, 3]

#mul of the list elements
import functools
import operator
L = [1, 2, 3]
print(L)
p=functools.reduce(operator.mul,L)
print(p)                                                                 #6


