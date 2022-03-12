#if else
#Q1 even or odd
n=int(input())                  #3 , 6
if n % 2 == 1:
    print("ODD")                #ODD
else:
    print("EVEN")               #EVEN

#Q2
n=int(input("Enter number="))       #Enter number=-4
print(abs(n))                       #4

#Q3
a=int(input("a="))                                      #a=4
b=int(input("b="))                                      #b=5
c=int(input("c="))                                      #c=6
if a>b and a>c:
    print(" ",a,"greater than ",b,",",c)
elif b>c and b>a:
    print(" ", b, "greater than ", a, ",", c)
else:
    print(" ",c,"greater than ",a,",",b)                #6 greater than  4 , 5

#Q4
year=int(input("Enter Year="))                      #Enter Year=2016,1998
if year%4==0 and year%100!=0 or year%400==0:
    print(" ",year,"is a leap year")                #2016 is a leap year
else:
    print(" ", year, "is not a leap year")          #1998 is not a leap year

#Q5
n=float(input("Enter n="))                          #Enter n=0.1,0,-4
if n>0:
    print(" ",n,"is positive")                      #0.1 is positive
elif n==0:
    print(" ", n, "is zero")                        #0.0 is zero
else:
    print(" ", n, "is negative")                    #-4.0 is negative

#Q6
a=float(input("Enter marks of English="))              #Enter marks of English=32,50,45,70
b=float(input("Enter marks of Maths="))                #Enter marks of Maths=50,55,50,80
c=float(input("Enter marks of Science="))              #Enter marks of Science=22,60,55,90
d=float(input("Enter marks of Social studies="))       #Enter marks of Social studies=4,65,60,85
e=float(input("Enter marks of Hindi/Marathi="))        #Enter marks of Hindi/Marathi=5,75,60,75
avg= (a+b+c+d+e)/500*100
if avg>=75:
    print("Passed with Distinction ",avg)              #Passed with Distinction  80.0
elif avg>=60:
    print("Passed with First class ",avg)              #Passed with First class  60.0
elif avg>=45:
    print("Passed with Second Class ",avg)             #Passed with Second Class  54.0
elif avg<35:
    print("Failed ",avg)                               #Failed  22.6
