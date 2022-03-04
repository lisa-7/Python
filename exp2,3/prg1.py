#exp2
print("Lisa")                                   #Lisa
print("MSBTE")                                  #MSBTE

#exp3
#Q1 us to dollar
dollar= float(input("enter dollars="))          #enter dollars=50
rupees= dollar*70
print("Rupees=",rupees)                         #Rupees= 3500.0

#Q2 bits to kb,mb,gb,tb
bit= int(input("Enter bits="))                  #Enter bits=10000000000
kb=bit/8000
mb=kb/1000
gb= mb/1000
tb= gb/1000
print("kb=",kb)                                 #kb= 1250000.0
print("mb=",mb)                                 #mb= 1250.0
print("gb=",gb)                                 #gb= 1.25
print("tb=",tb)                                 #tb= 0.00125

#Q3 squar of num
num= int(input("Enter number"))                 #Enter number4
sq= num**2
print("SQ of ", num, "is =",sq)                 #SQ of  4 is = 16

#Q4 area of rectangle
L=int(input("l="))                              #l=4
B=int(input("b="))                              #b=4
A=L*B
print("Area=",A)                                #Area= 16

#Q5 area and perimeter of square
side=int(input("Side="))                        #Side=4
A=side*side
P=4*side
print("Area=",A)                                #Area= 16
print("Perimeter=",P)                           #Perimeter= 16

#Q6 area and surface
pi=float(22/7)
h=float(input("Height="))                       #Height=4
r=float(input("Radious="))                      #Radious=6
a=(2*pi*r*h)+(pi*(r**2)*2)
print("Area=",a)                                #Area= 377.1428571428571
v=pi*r*r*h
print("Volume=",v)                              #Volume= 452.57142857142856

#Q7 swap value of 2 variable
x=int(input("x="))                              #x=int(input("x="))                              #
y=int(input("y="))                              #y=5
temp=x
x=y
y=temp
print("the value of x after swap=",x)           #the value of x after swap= 5
print("the value of y after swap=",y)           #the value of y after swap= 10