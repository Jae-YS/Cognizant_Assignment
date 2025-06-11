def greet_user(name):
    print(f"Hello, {name}! Welcome aboard.")


def add_numbers(a, b):
    return a + b


def describe_pet(pet_name, animal_type="dog"):
    print(f"I have a {animal_type} named {pet_name}.")


def make_sandwich(*ingredients):
    print("Making a sandwich with the following ingredients:")
    for ingredient in ingredients:
        print(f"- {ingredient}")


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    greet_user("Alice")
    result = add_numbers(5, 10)
    print(f"The sum of 5 and 10 is {result}.")

    describe_pet("Buddy")
    describe_pet("Whiskers", "cat")

    make_sandwich("Lettuce", "Tomato", "Cheese")

    print(f"Factorial of 5 is {factorial(5)}.")
    print(f"The 6th Fibonacci number is {fibonacci(6)}.")


if __name__ == "__main__":
    main()
