num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Asking the user to select an operation
operation = input("Choose the operation (+, -, *, /): ")

# Performing the calculation using a match-case statement
match operation:
    case '+':
        result = num1 + num2
        print(f"The result is {result}")
    case '-':
        result = num1 - num2
        print(f"The result is {result}.")
    case '*':
        result = num1 * num2
        print(f"The result is {result}.")
    case '/':
        if num2 != 0:
            result = num1 / num2
            print(f"The result is {result}.")
        else:
            print("Cannot divide by zero.")
    case _:
        print("Invalid operation. Please choose one of the following: +, -, *, /.")
