# Data Types
number = 45  # int
num = 54.76  # float
greeting = "hello there"  # str
is_python_interesting = True  # bool
# variable storing multiple values
languages = ["python", "php", "javascript"]  # list
fruits = ("apple", "mellon", "pineapple")  # Tuple
countries = {"kenya", "china", "USA"}  # set
# Dictionary
details = {
    "firstname": "Grace",
    "age": 17,
    "course": "MIT",
    "nationality": "North America"
}

print(number)
print(greeting)
print(countries)
print(is_python_interesting)
print(details["course"])
print(details["nationality"])

# determining a data type
print(type(details))
print(type(countries))
# Type casting - converting one data type to another data type
print(float(number))
print(int(num))
