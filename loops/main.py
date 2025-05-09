def countdown():
    # This function counts down from a given number to 1
    num = int(input("Enter a start number: "))
    while num > 0:
        print(num)
        num -= 1
    print("Blast off!")


def multiplication_table():
    # This function prints the multiplication table for a given number
    num = int(input("Enter a number: "))

    # Using a for loop to print the multiplication table
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")


def factorial():
    # This function calculates the factorial of a given number
    num = int(input("Enter a number: "))

    result = 1

    # Using a for loop to calculate the factorial
    for i in range(1, num + 1):
        result *= i

    print(f"The factorial of {num} is {result}")


def main():
    countdown()
    multiplication_table()
    factorial()


if __name__ == "__main__":
    main()
