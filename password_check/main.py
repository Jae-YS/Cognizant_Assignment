import string


def get_password():
    """
    Prompt the user for a password and return it.
    """
    password = input("Enter your password: ")
    return password


def has_special_char(password):
    """
    Check if the password contains at least one special character.
    """
    return any(c in string.punctuation for c in password)


def check_password(password):
    """
    Check the password for strength and return a score.
    The score is based on the following criteria:
    - Length: 2 points for >= 10 characters, 1 point for >= 8 characters
    - Special character: 2 points for at least one special character
    - Uppercase letter: 2 points for at least one uppercase letter
    - Lowercase letter: 2 points for at least one lowercase letter
    - Digit: 2 points for at least one digit
    """
    errors = []
    score = 0

    # Length check
    if len(password) >= 10:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        errors.append(f"{password} is {8 - len(password)} characters too short")

    # Special character
    if has_special_char(password):
        score += 2
    else:
        errors.append(f"{password} does not contain a special character")

    # Uppercase
    if any(c.isupper() for c in password):
        score += 2
    else:
        errors.append(f"{password} does not contain an uppercase letter")

    # Lowercase
    if any(c.islower() for c in password):
        score += 2
    else:
        errors.append(f"{password} does not contain a lowercase letter")

    # Digit
    if any(c.isdigit() for c in password):
        score += 2
    else:
        errors.append(f"{password} does not contain a digit")

    print(f"Password strength score: {score}/10")

    if score == 10:
        print(f"Password is valid: {password}")
    else:
        print("\n".join(errors))


def main():
    password = get_password()
    check_password(password)


if __name__ == "__main__":
    main()
