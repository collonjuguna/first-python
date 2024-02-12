# calculator programme
# This function adds two numbers
def add(x, y):
    return x + y


# This function subtracts two numbers
def subtract(x, y):
    return x - y


# This function multiplies two numbers
def multiply(x, y):
    return x * y


# This function divides two numbers
def divide(x, y):
    return x / y


print(" operation.")
print("+.Add")
print("-.Subtract")
print("*.Multiply")
print("/.Divide")

while True:
    #  choice(+/-/*//):
    choice = input("Enter choice(+/-/*//): ")

    if choice in ('+', '-', '*', '/'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid . enter a number.")
            continue

        if choice == '+':

            sum = (num1 + num2)
            print(sum)

        elif choice == '-':
            sub = (num1 - num2)
            print(sub)
        elif choice == '*':
            mult = (num1 * num2)
            print(mult)

        elif choice == '/':
            div = (num1 / num2)
            print(div)

        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break
    else:
        print("Invalid Input")
