# Inbuilt functions
number = max(87, 56, 68, 12, 123)
print(number)
x = min(68, 34, 2, 675, 87)
print(x)
y = pow(2, 4)
print(y)


# user-defined function
def detail():
    print("collins")


detail()  # calling a function to print the result


def student():
    name = "vincent"
    age = 18
    course = "MIT"
    print(name, age, course)


student()


# parameters
def students(name, age, course):
    print(name, age, course)


students("vincent", 18, "MIT")
students("collins", 18, "MIT")
students("brian", 18, "MIT")
students("john", 18, "MIT")


def employees(fullname, age, gender, position, salary):
    print(fullname, age, gender, position, salary)

employees("moses karanja", 32, "male", "manager", 1500)
employees("maurice murioki", 41, "male", "supervisor", 1500)
employees("mercy njeri", 21, "female", "land manager", 23000)
employees("maxwell njuguna", 29, "male", "farm input consultant", 20000)
employees("magdalene wambui", 20, "female", "land consultant", 12000)

