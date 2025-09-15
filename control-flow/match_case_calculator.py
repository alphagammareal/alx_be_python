# Prompt for user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
symb = input("Choose the operation (+, -, *, /): ")

# Perform the calculation using match case
match symb:
    case "+":
        results = num1 + num2
        print("The result is ", results)
    case "-":
        results = num1 - num2
        print("The result is ", results)
    case "*":
        results = num1 * num2
        print("The result is ", results)
    case "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            results = num1 / num2
            print("The result is ", results)
    case _:
        print("Invalid Symbol")