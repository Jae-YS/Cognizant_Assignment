import random


def check_guess(guess, number_to_guess) -> bool:
    """This function checks if the user's guess is correct."""
    if guess < number_to_guess:
        print("Too low! Try again.")
    elif guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the number!")
        return True
    return False


def main():
    number_to_guess = random.randint(1, 100)

    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Can you guess it?")

    attempts = 0
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if check_guess(guess, number_to_guess):
                print(f"You guessed the number in {attempts} attempts!")
                break
        except ValueError:
            print("Please enter a valid integer.")


if __name__ == "__main__":
    main()
