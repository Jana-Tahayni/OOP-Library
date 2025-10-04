from models.library import Library
from exceptions.itemNotAvailableError import ItemNotAvailableError
from exceptions.itemNotFoundError import ItemNotFoundError
from exceptions.userNotFoundError import UserNotFoundError

def main():
    lib = Library()
    lib.Load()

    while True:
        print("\n--- Library Management System ---")
        print("1. View all available items")
        print("2. Search item by title or type")
        print("3. Register a new user")
        print("4. Borrow an item")
        print("5. Reserve an item")
        print("6. Return an item")
        print("7. Add new item")
        print("8. Remove item")
        print("9. Remove user")
        print("10. Exit and Save")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                for item in lib.items:
                    if item.check_availability():
                        item.display_info()

            elif choice == "2":
                keyword = input("Enter title keyword or item type (Book/DVD/Magazine): ").lower()
                found = False 
                for item in lib.items:
                    if keyword in item.Title.lower() or keyword == item.__class__.__name__.lower():
                        item.display_info()
                        found = True
                if not found:
                    print("No matching items found.")

            elif choice == "3":
                name = input("Enter user name: ")
                email = input("Enter user email: ")
                user = lib.AddUser(name, email)
                print(f"User registered with ID: {user.UserID}")

            elif choice == "4":
                user_id = input("Enter your user ID: ")
                item_id = input("Enter item ID to borrow: ")
                lib.BorrowItem(user_id, item_id)
                print("Item borrowed successfully.")

            elif choice == "5":
                user_id = input("Enter your user ID: ")
                item_id = input("Enter item ID to reserve: ")
                lib.ReserveItem(user_id, item_id)
                print("Item reserved successfully.")

            elif choice == "6":
                user_id = input("Enter your user ID: ")
                item_id = input("Enter item ID to return: ")
                lib.ReturnItem(user_id, item_id)
                print("Item returned successfully.")

            elif choice == "7":
                item_type = input("Enter item type (Book/DVD/Magazine): ")
                item_id = input("Enter item ID: ")
                title = input("Enter title: ")
                author = input("Enter author: ")
                if item_type == "Book":
                    page_num = input("Enter number of pages: ")
                    generation = input("Enter generation: ")
                    lib.AddItem(item_type, item_id, title, author, page_num, generation)
                elif item_type == "DVD":
                    duration = input("Enter duration in minutes: ")
                    year = input("Enter year: ")
                    lib.AddItem(item_type, item_id, title, author, duration, year)
                elif item_type == "Magazine":
                    year = input("Enter publication year: ")
                    company = input("Enter publishing company: ")
                    lib.AddItem(item_type, item_id, title, author, year, company)
                else:
                    print("Invalid item type.")

            elif choice == "8":
                item_id = input("Enter item ID to remove: ")
                try:
                    lib.RemoveItem(item_id)
                    print("Item removed successfully.")
                except ItemNotFoundError:
                    print("Item not found. Please check the ID.")

            elif choice == "9":
                user_id = input("Enter user ID to remove: ")
                try:
                    lib.RemoveUser(user_id)
                    print("User removed successfully.")
                except UserNotFoundError:
                    print("User not found. Please check the ID.")

            elif choice == "10":
                lib.Store()
                print("Data saved. Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
