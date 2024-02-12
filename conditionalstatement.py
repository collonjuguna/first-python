temperature = 13
if temperature > 25:
    print("it's hot")
else:
    print("it's cold")
# A programme that returns the largest number among three numbers
num1 = 10
num2 = 96
num3 = 21
if num1 > num2 and num1 > num3:
    print(num1, "is the largest")
elif num2 > num1 and num2 > num3:
    print(num2, "is the largest")
else:
    print(num3, "is the largest number")

# A program checking an even or odd
number = 21
if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")
# Assignment
a = 'cat'
print(a)
a = a + 'in a hat'
print(a)
b = 'new string'
print(b)
b = 'this is a ' + b[0:]
a = 'python'
a = a.replace('ython','rogramming')
print(a)

b = a.replace('rogramming','rogrammer')
print(b)








#program checking whether a number is prime or not

a1 = 1
a2 = 2
a3 = 3
if a1 < a2 and a1 < a3:
    print(a1, "is not prime")
elif a1 > a2 and a1 > a3:
    print(a1,"is a prime number")
else:
    print(a3,"is a prime")