# experiment no 6 List
#concatenate list


L1 = [1, 2, 3]
print(L1)                                                              #[1, 2, 3]
L2 = [4, 5, 6, 7, 8, 9]
print(L2)                                                              #[ 4, 5, 6, 7, 8, 9]

# + operator
L3=L1+L2
print(L3)                                                              #[1, 2, 3, 4, 5, 6, 7, 8, 9]

#by append
for x in L2:
    L1.append(x)
print(L1)                                                              #[1, 2, 3, 4, 5, 6, 7, 8, 9]

#by extend
L1 = [1, 2, 3]
print(L1)                                                              #[1, 2, 3]
L2 = [4, 5, 6, 7, 8, 9]
print(L2)                                                              #[ 4, 5, 6, 7, 8, 9]
L1.extend(L2)
print(L1)                                                              #[1, 2, 3, 4, 5, 6, 7, 8, 9]

#by list comprehension
L1 = [1, 2, 3]
print(L1)                                                              #[1, 2, 3]
L2 = [4, 5, 6, 7, 8, 9]
print(L2)                                                              #[ 4, 5, 6, 7, 8, 9]
L3= [y for x in[L1,L2] for y in x]
print(L3)                                                              #[1, 2, 3, 4, 5, 6, 7, 8, 9]

#using * operator
L1 = [1, 2, 3]
print(L1)                                                              #[1, 2, 3]
L2 = [4, 5, 6, 7, 8, 9]
print(L2)                                                              #[ 4, 5, 6, 7, 8, 9]
L3=[*L1,*L2]
print(L3)                                                              #[1, 2, 3, 4, 5, 6, 7, 8, 9]

#using import itertools
import itertools
L1 = [1, 2, 3]
print(L1)                                                              #[1, 2, 3]
L2 = [4, 5, 6, 7, 8, 9]
print(L2)                                                              #[ 4, 5, 6, 7, 8, 9]
L3 = list(itertools.chain(L1,L2))
print(L3)                                                              #[1, 2, 3, 4, 5, 6, 7, 8, 9]
