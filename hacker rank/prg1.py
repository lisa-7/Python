
#even odd
n = int(input())
if n % 2 == 1:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")

#arithmetic
a = int(input())
b = int(input())
print(a + b)
print(a - b)
print(a * b)

a = int(input())
b = int(input())
print(a // b)
print(a / b)
