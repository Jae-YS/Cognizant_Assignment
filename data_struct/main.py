def learning_list():
    fruits = ["mango", "strawberry", "blueberry", "pineapple", "grape"]

    print("Original list:", fruits)

    fruits.append("kiwi")
    print("After adding a fruit:", fruits)

    fruits.remove("mango")
    print("After removing a fruit:", fruits)

    print("Reversed list:", fruits[::-1])


def learning_dict():
    my_info = {"name": "Steven", "age": 28, "city": "Los Angeles"}

    my_info["favorite color"] = "Green"

    my_info["city"] = "New York"

    print("\nKeys:", ", ".join(my_info.keys()))
    print("Values:", ", ".join(str(value) for value in my_info.values()))


def learning_tuple():
    favorite_things = ("Interstellar", "Imagine", "Sapiens")
    print("\nFavorite things:", favorite_things)

    try:
        favorite_things[0] = "Inception"
    except TypeError:
        print("Tuples cannot be changed.")

    print("Length of tuple:", len(favorite_things))


def main():
    learning_list()
    learning_dict()
    learning_tuple()


if __name__ == "__main__":
    main()
