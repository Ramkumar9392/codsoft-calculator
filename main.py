def calculator():
    """Performs basic arithmetic operations based on user input."""

    operation = input('''
Please select an operation:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

    number_1 = float(input("Enter your first number: "))
    number_2 = float(input("Enter your second number: "))

    if operation == '+':
        print(number_1 + number_2)
    elif operation == '-':
        print(number_1 - number_2)
    elif operation == '*':
        print(number_1 * number_2)
    elif operation == '/':
        if number_2 == 0:
            print("Error: Division by zero")
        else:
            print(number_1 / number_2)
    else:
        print("Invalid operation")

    # Offer to perform another calculation
    again = input("Do you want to perform another calculation? (yes/no): ")
    if again.lower() == "yes":
        calculator()

calculator()  # Call the function to start the calculator
