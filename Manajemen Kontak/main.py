from process import ContactManager
from view import ContactView

def main():
    manager = ContactManager()
    view = ContactView()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Delete Contact")
        print("4. Search Contact")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            try:
                name = input("Enter name: ")
                phone = input("Enter phone: ")
                email = input("Enter email: ")
                manager.add_contact(name, phone, email)
                view.display_message("Contact added successfully!")
            except ValueError as e:
                view.display_message(f"Error: {e}")
        elif choice == "2":
            view.display_contacts(manager.contacts)
        elif choice == "3":
            try:
                index = int(input("Enter contact number to delete: "))
                manager.delete_contact(index)
                view.display_message("Contact deleted successfully!")
            except (ValueError, IndexError) as e:
                view.display_message(f"Error: {e}")
        elif choice == "4":
            keyword = input("Enter keyword to search: ")
            results = manager.search_contact(keyword)
            if results:
                view.display_contacts(results)
            else:
                view.display_message("No contacts found.")
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            view.display_message("Invalid option. Please try again.")

if __name__ == "__main__":
    main()