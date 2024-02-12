try:
    print(x)
except:
    print("name error occurred")

num1 = 20
num2 = 0

try:
    print(num1 / num2)
except:
    print("zero division error occurred")

finally:
    print("success")

# user_defined functions
try:
    def multiply(x, y):
        return x * y
except:
    print("exception occurred")
finally:
    print("success")

print(multiply(10, 20))
