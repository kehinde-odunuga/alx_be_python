# Create a Python script that implements a simple interface for managing a shopping list.
# This task focuses on using lists to store and manipulate data dynamically.

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            item = input("Enter the item to add: ").lower()
            shopping_list.append(item)
            print(f"{item} has been successfully added to your shopping list")
        elif choice == '2':
            # Prompt for and remove an item
            item = input("Enter the item to remove: ").lower()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} has been successfully removed from your shopping list")
            else:
                print(f"{item} is not in your shopping list")
        elif choice == '3':
            # Display the shopping list
            if shopping_list == []:
                print("You do not have any item at the moment. Add some items to your list")
            else:
                print(f"This is your shopping list here: {shopping_list}")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()