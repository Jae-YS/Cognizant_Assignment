import logging

# Configure logging to write error messages to a file
logging.basicConfig(filename="error_log.txt", level=logging.ERROR)


def get_number(prompt):
    """Prompt the user for a number, ensuring valid input."""
    while True:
        try:
            return float(input(prompt))  # Try converting user input to float
        except ValueError as e:
            print("Invalid input! Please enter a valid number.")
            logging.error(f"ValueError occurred: {e}")  # Log invalid input error


# Basic arithmetic operations
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    """Divide two numbers safely, handling division by zero."""
    try:
        return a / b
    except ZeroDivisionError as e:
        print("Oops! Division by zero is not allowed.")
        logging.error(f"ZeroDivisionError occurred: {e}")  # Log division by zero error
        return None


def display_menu():
    """Display the calculator options menu."""
    print("\nWelcome to the Error-Free Calculator!")
    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")


def main():
    """Main program loop for the calculator."""
    while True:
        display_menu()  # Show the menu to the user
        choice = input("> ")

        if choice == "5":
            print("Goodbye!")  # Exit the loop if user selects 5
            break

        if choice not in {"1", "2", "3", "4"}:
            print("Invalid selection. Please choose a number between 1 and 5.")
            continue  # Skip to next loop iteration for invalid menu choice

        # Prompt user for two valid numbers
        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")

        try:
            # Perform the selected operation
            if choice == "1":
                result = add(num1, num2)
                operation = "Addition"
            elif choice == "2":
                result = subtract(num1, num2)
                operation = "Subtraction"
            elif choice == "3":
                result = multiply(num1, num2)
                operation = "Multiplication"
            elif choice == "4":
                result = divide(num1, num2)
                operation = "Division"

            # Only display the result if the operation didn't fail (e.g., division by zero)
            if result is not None:
                print(f"The result of {operation.lower()} is {result}")
        except Exception as e:
            # Catch any unexpected errors and log them
            print("An unexpected error occurred.")
            logging.error(f"Unhandled exception: {e}")
        finally:
            # This block runs no matter what
            print("Operation complete.\n")


# Run the program
if __name__ == "__main__":
    main()
