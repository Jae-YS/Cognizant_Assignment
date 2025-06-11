import turtle


# Step 2: Recursive Factorial Function
def factorial(n):
    """Returns the factorial of a number using recursion."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# Step 3: Recursive Fibonacci Function
def fibonacci(n):
    """Returns the nth Fibonacci number using recursion."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# Step 4: Recursive Fractal Drawing (Bonus)
def draw_fractal_tree(branch_length, t):
    """Draws a recursive fractal tree using the turtle module."""
    if branch_length > 5:
        t.forward(branch_length)
        t.right(20)
        draw_fractal_tree(branch_length - 15, t)
        t.left(40)
        draw_fractal_tree(branch_length - 15, t)
        t.right(20)
        t.backward(branch_length)


# Input validation for positive integers
def get_positive_integer(prompt):
    while True:
        try:
            num = int(input(prompt))
            if num < 0:
                raise ValueError
            return num
        except ValueError:
            print("Please enter a valid non-negative integer.")


# Menu loop
def main():
    print("Welcome to the Recursive Artistry Program!")

    while True:
        print("\nChoose an option:")
        print("1. Calculate Factorial")
        print("2. Find Fibonacci")
        print("3. Draw a Recursive Fractal")
        print("4. Exit")

        choice = input("> ")

        if choice == "1":
            num = get_positive_integer("Enter a number to find its factorial: ")
            result = factorial(num)
            print(f"The factorial of {num} is {result}.")

        elif choice == "2":
            num = get_positive_integer("Enter the position of the Fibonacci number: ")
            result = fibonacci(num)
            print(f"The {num}th Fibonacci number is {result}.")

        elif choice == "3":
            print("Drawing a simple fractal tree... 🌳")
            screen = turtle.Screen()
            t = turtle.Turtle()
            t.left(90)
            t.speed("fastest")
            draw_fractal_tree(100, t)
            screen.exitonclick()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
