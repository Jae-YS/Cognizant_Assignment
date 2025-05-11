def slice_index(s):

    # Slicing the string
    first_six = s[0:6]

    # Slicing the string to get the third word
    amazing = s[10:17]

    # Slicing the string to get the reversed string
    reversed = s[::-1]

    print(f"First six characters: {first_six}")
    print(f"Third word: {amazing}")
    print(f"Reversed string: {reversed}")


def string_methods(s):
    # Converting to uppercase
    upper = s.upper()

    # stripping whitespace
    strip = s.strip()

    # Capitalizing the first letter of the string
    capitalize = s.capitalize()

    # replacing "world" with "universe"
    replaced = s.replace("world", "universe")

    print(f"Uppercase: {upper}")
    print(f"Stripped: {strip}")
    print(f"Capitalized: {capitalize}")
    print(f"Replaced: {replaced}")


def valid_palindrome():
    s = input("Enter a string: ")

    if s.strip() == s.strip()[::-1]:
        print(f"{s} is a palindrome")
    else:
        print(f"{s} is not a palindrome")


def main():
    s = "Python is amazing!"
    t = "   Hello world!   "

    slice_index(s)
    string_methods(t)
    valid_palindrome()


if __name__ == "__main__":
    main()
