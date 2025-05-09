def check_age(num):
    """This function checks if the user is eligible to vote based on their age."""

    # Check if the user is eligible to vote
    if num > 18:
        print("Congratulations! You are eligible to vote. Go make a difference!")
    else:
        print(
            f"Oops! You’re not eligible yet. But hey, only {18 - num} more years to go!"
        )


def main():
    # This is a simple program to check if a user is eligible to vote
    print("Welcome to the Voting Eligibility Checker!")

    # get the user age, convert it to int and store it in a variable
    num = int(input("How old are you? "))

    # check if the user is eligible to vote by calling the check_age function
    check_age(num)


if __name__ == "__main__":
    main()
