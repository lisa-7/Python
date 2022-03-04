# experiment no 6 List
L = [1, 2, 3]
print(L)                                                                #[1, 2, 3]

#add single element to the end of the list
L.append(4)
print(L)                                                                #[1,2,3,4]

#insert element any where in the list
L.insert(3,"a")
print(L)                                                                #[1, 2, 3, 'a', 4]

#add multiple elements at the end of the list
L.extend([5,6,6])
print(L)                                                                #[1, 2, 3, 'a', 4, 5, 6, 6]

#shows lenght
print("length =",len(L))                                                #length = 8

#removes element from list
L.remove("a")
print(L)                                                                #[1, 2, 3, 4, 5, 6, 6]

L.remove(6)
print(L)                                                                #[1, 2, 3, 4, 5, 6]

#reverse
L.reverse()
print(L)                                                                #[6, 5, 4, 3, 2, 1]

#sum of the list elements
print("sum of list elements =",sum(L))                                  #sum of list elements = 21

#sort program
#sort acending
L2 = [39,5,72,15,33,65,9,11,100]
L2.sort()
print(L2)                                                               #[5, 9, 11, 15, 33, 39, 65, 72, 100]

#sort decending
L2.sort(reverse=True)
print(L2)                                                               #[100, 72, 65, 39, 33, 15, 11, 9, 5]

#counting elements in list
print("L List count of 6=", L.count(6))                                 #L List count of 6= 1
print("L2 List count of 3=", L2.count(3))                               #L2 List count of 3= 0

#pop
#pop works from idex number
L3 = [1,2,3,4,5,6,7,8,9]
print(L3)                                                               #[1, 2, 3, 4, 5, 6, 7, 8, 9]
print("pop() element =", L3.pop())                                      #pop() element = 9
print(L3)                                                               #[1, 2, 3, 4, 5, 6, 7, 8]
print("pop(1) element =", L3.pop(1))                                    #pop(1) element = 2
print(L3)                                                               #[1, 3, 4, 5, 6, 7, 8]
print("pop(-1) element =", L3.pop(-1))                                  #pop(-1) element = 8
print(L3)                                                               #[1, 3, 4, 5, 6, 7]

#index
print("index of 3=", L3.index(3))                                       #index of 3= 1