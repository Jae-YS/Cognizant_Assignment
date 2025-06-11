# Function to display the current inventory
def display_inventory(inventory):
    print("Updated inventory:")
    if not inventory:
        print("No items in inventory.")
    else:
        for item, quantity in inventory.items():
            print(f"{item}: {quantity[0]} (Price: ${quantity[1]:.1f})")


# Function to add an item to the inventory
def add_item(inventory, item_name, quantity, price):
    if item_name in inventory:
        # If item exists, update the quantity
        inventory[item_name][0] += quantity
    else:
        # Add new item as a [quantity, price] list
        inventory[item_name] = [quantity, price]
    print(f"Added {quantity} of {item_name} at ${price:.1f} each.")
    display_inventory(inventory)


# Function to remove an item from the inventory
def remove_item(inventory, item_name):
    if item_name in inventory:
        del inventory[item_name]  # Remove item completely
        print(f"{item_name} is now out of stock and removed from inventory.")
    else:
        print(f"{item_name} not found in inventory.")
    display_inventory(inventory)


# Function to update an existing item with new quantity and price
def update_item(inventory, item_name, quantity, price):
    if item_name in inventory:
        inventory[item_name] = [quantity, price]  # Replace old values
        print(f"Updated {item_name} to {quantity} at ${price:.1f} each.")
    else:
        print(f"{item_name} not found in inventory.")
    display_inventory(inventory)


# Function to calculate the total value of the inventory
def calculate_total_value(inventory):
    total_value = sum(quantity * price for quantity, price in inventory.values())
    print(f"Total inventory value: ${total_value:.2f}")
    return total_value


# Main loop to interact with the user
def run_inventory():
    inventory = {}  # Start with an empty inventory

    print("Welcome to the Inventory Manager!")
    while True:
        print(
            "1. Add item, 2. Remove item, 3. Update item, 4. Display inventory, 5. Exit"
        )
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            # Add item
            item_name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: "))
            add_item(inventory, item_name, quantity, price)
        elif choice == "2":
            # Remove item
            item_name = input("Enter item name to remove: ")
            remove_item(inventory, item_name)
        elif choice == "3":
            # Update item
            item_name = input("Enter item name to update: ")
            quantity = int(input("Enter new quantity: "))
            price = float(input("Enter new price: "))
            update_item(inventory, item_name, quantity, price)
        elif choice == "4":
            # Display inventory
            display_inventory(inventory)
        elif choice == "5":
            # Exit the program
            print("Exiting Inventory Manager.")
            break
        else:
            print("Invalid option. Please try again.")

        # Show total inventory value after each action
        calculate_total_value(inventory)


def main():
    run_inventory()


if __name__ == "__main__":
    main()
