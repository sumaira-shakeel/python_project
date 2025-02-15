def calculator(num1, num2, operation):
    if operation == "addition":
        return num1 + num2
    elif operation == "subtraction":
        return num1 - num2
    elif operation == "multiplication":
        return num1 * num2
    elif operation == "division":
        if num2 == 0:
            return "Error: Division by zero is not allowed"
        return num1 / num2
    else:
        return "Invalid operation"

# Main program
def main():
    print("Welcome to my Python calculator")
    num1 = float(input("Enter your first number: "))
    num2 = float(input("Enter your second number: "))
    print("Choose the operation you want to perform: addition, subtraction, multiplication, division")
    operation = input("Enter your operation: ").strip().lower()
    result = calculator(num1, num2, operation)
    # The f in Python strings stands for formatted string literals or f-strings. They were introduced in Python 3.6 to make it easier and cleaner to include variables inside strings.

# Why Use f-strings?
# Cleaner Syntax: No need for complex concatenation using + or str.format().
# Readability: Code becomes more readable.
# Efficiency: Faster than older formatting methods (% or .format()).

    print(f"The result of {operation} is: {result}")

# Call the main function to run the program
main()

       