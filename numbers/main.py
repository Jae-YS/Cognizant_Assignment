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

    valid_input = False
    attempts = 0
    while attempts < 10:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            valid_input = check_guess(guess, number_to_guess)
            if valid_input:
                print(f"You guessed the number in {attempts} attempts!")
                break
        except ValueError:
            print("Please enter a valid integer.")

    if valid_input is False:
        print(f"You've used all your attempts. The number was {number_to_guess}.")
    else:
        print("Thanks for playing!")


if __name__ == "__main__":
    main()
