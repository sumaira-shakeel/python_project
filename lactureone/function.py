# functions in python
def greet():
    for _ in range(3):  # Runs 3 times
        print(f"Hello, this is Sumaira Shakeel!")

greet()
def greet(n):
    if n == 0:  # Base condition to stop recursion
        return
    print(f"Hello, this is Sumaira Shakeel!")
    greet(n - 1)  # Calling function with a reduced value

greet(3)  # Function will run 3 times
#  What Are Parameters and Arguments?
# 📌 Parameters and arguments are used in functions to pass data.
# 📌 Parameters are placeholders inside a function definition.
# 📌 Arguments are the actual values passed when calling a function.



def greet(name):  # 'name' is a parameter
    print(f"Hello, {name}!")

greet("Sumaira")  # "Sumaira" is an argument
greet("Ali")      # "Ali" is an argument

def info(name,age):
    print(f"my name is {name} and my age is {age}")


info("sumaira",38) 
# fuction inside afunction
# A function can be defined inside another function. This is known as a nested function.
def outer():
    def inner():
        return "Hello from inner function!"
    return inner  # Returning inner function without calling it

# Assign returned function to a variable
my_function = outer()
print(my_function())  # Calling inner function
def calculator(operation):
    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    if operation == "add":
        return add  # Returning `add` function
    else:
        return subtract  # Returning `subtract` function

# Get the function
func = calculator("add")
print(func(10, 5))  # Output: 15



  