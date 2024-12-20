def add_contact(contacts, name, phone, email):
    if name in contacts:
        print(f"Contact with the name '{name}' already exists.")
    else:
        contacts[name] = {"Phone": phone, "Email": email}
        print(f"Contact '{name}' added successfully.")

def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
    else:
        print("\nContact List:")
        for name, details in contacts.items():
            print(f"Name: {name}, Phone: {details['Phone']}, Email: {details['Email']}")

def search_contact(contacts, name):
    contact = contacts.get(name)
    if contact:
        print(f"\nFound Contact: Name: {name}, Phone: {contact['Phone']}, Email: {contact['Email']}")
    else:
        print(f"Contact with the name '{name}' not found.")

def update_contact(contacts, name, phone=None, email=None):
    if name in contacts:
        if phone:
            contacts[name]["Phone"] = phone
        if email:
            contacts[name]["Email"] = email
        print(f"Contact '{name}' updated successfully.")
    else:
        print(f"Contact with the name '{name}' does not exist.")

def delete_contact(contacts, name):
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully.")
    else:
        print(f"Contact with the name '{name}' does not exist.")

def main():
    contacts = {}

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            add_contact(contacts, name, phone, email)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            name = input("Enter the name to search: ")
            search_contact(contacts, name)
        elif choice == "4":
            name = input("Enter the name to update: ")
            phone = input("Enter new phone number (or press Enter to skip): ")
            email = input("Enter new email address (or press Enter to skip): ")
            update_contact(contacts, name, phone if phone else None, email if email else None)
        elif choice == "5":
            name = input("Enter the name to delete: ")
            delete_contact(contacts, name)
        elif choice == "6":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
