

"""
#sum of 4 entered no.
sum=0.0
for i in range(1,6):
    print("Enter no=", end=" ")
    n=input()
    sum=sum+float(n)
print("\n sum=",sum)

Enter no= 4
Enter no= 4
Enter no= 4
Enter no= 4
Enter no= 4

 sum= 20.0

#4stars
for i in range(1,5):
    print("*", end="")                      #****
"""
"""
#star in row
for i in range(1,5):
    for j in range (1,5):
        print("*", end=" ")
    print()

* * * *
* * * *
* * * *
* * * *

#incrementing star
for i in range(1,5):
    for j in range (1,i+1):
        print("* ", end=" ")
    print()

*
*  *
*  *  *
*  *  *  *

#for decrementing star
for i in range(4,0,-1):
    for j in range (1,i+1):
        print("* ", end=" ")
    print()

*  *  *  *
*  *  *
*  *
*
"""
#star pyramid
for i in range(1,5):
    for j in range (1,5):
        print("_", end=" ")
    for k in range(1, i+1):
        print("*", end=" ")
    print()

