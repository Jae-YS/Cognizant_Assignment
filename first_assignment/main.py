def greet(name, age, height):
    print(f"Hello, {name}! You are {age} years old and {height} feet tall.")


def arithmetic_operations(a, b):
    sum_result = a + b
    diff_result = a - b
    prod_result = a * b
    div_result = a / b if b != 0 else "undefined"

    print(f"Sum: {sum_result}")
    print(f"Difference: {diff_result}")
    print(f"Product: {prod_result}")
    print(f"Division: {div_result}")


def conditional():
    num = int(input("Enter a number: "))
    if num > 0:
        print("The number is positive.")
    elif num < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")


def main():

    # Creating helper functions to not clutter the main function
    greet("Jae", 21, 6.1)
    arithmetic_operations(10, 5)
    conditional()


if __name__ == "__main__":
    main()
