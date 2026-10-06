def calculate_result(first_number, second_number):
    """Divide the first number by the second number."""
    try:
        first_number = float(first_number)
        second_number = float(second_number)

        if second_number == 0:
            print("Error: Cannot divide by zero.")
            return None

        result = first_number / second_number
        return result

    except ValueError:
        print("Error: Please enter valid numbers.")
        return None


number1 = input("Enter first number: ")
number2 = input("Enter second number: ")

result = calculate_result(number1, number2)

if result is not None:
    print("Result:", result)