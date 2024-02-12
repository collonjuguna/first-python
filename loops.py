# while loop
# increment
number = 5
while number <= 10:
    print(number)
    number += 1
# decrementing
num = 105
while num >= 100:
    print(num)
    num -= 1
# Break statement
x = 20
while x <= 25:
    print(x)
    if x == 24:
        break
    x += 1
# continue statement
y = 79
while y < 85:
    y += 1
    if y == 83:
        continue
    print(y)

# for loop
languages = ["python","java","c++"]
for z in languages:
    print(z)
# printing a range

for mynumber in range(5):
    print(mynumber)
for mynum in range(2,6):
    print(mynum)
# increasing numbers using for loop
for count in range(20,32,2,):
    print(count)
