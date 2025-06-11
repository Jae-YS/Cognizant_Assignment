def task1_divide_by_input():
    print("\nDivide 100 by User Input")
    while True:
        try:
            num = int(input("Enter a number: "))
            result = 100 / num
            print(f"100 divided by {num} is {result}.")
            break
        except ZeroDivisionError:
            print("Oops! You cannot divide by zero.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def task2_common_exceptions():
    print("\nRaise and Handle Common Exceptions")

    # IndexError
    try:
        my_list = [1, 2, 3]
        print(my_list[5])
    except IndexError:
        print("IndexError occurred! List index out of range.")

    # KeyError
    try:
        my_dict = {"name": "Alice"}
        print(my_dict["age"])
    except KeyError:
        print("KeyError occurred! Key not found in the dictionary.")

    # TypeError
    try:
        result = "hello" + 5
    except TypeError:
        print("TypeError occurred! Unsupported operand types.")


def task3_try_except_else_finally():
    print("\nDivision with Full Exception Handling")
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 / num2
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter valid numbers.")
    else:
        print(f"The result is {result}.")
    finally:
        print("This block always executes.")


def main():
    task1_divide_by_input()
    task2_common_exceptions()
    task3_try_except_else_finally()


if __name__ == "__main__":
    main()
