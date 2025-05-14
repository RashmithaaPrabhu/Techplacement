import json
import os

DATA_FILE = 'contacts.json'

def load_contacts():
    """Load contacts from a JSON file."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []

def save_contacts(contacts):
    """Save contacts to a JSON file."""
    with open(DATA_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    """Add a new contact."""
    name = input("Enter name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    phone = input("Enter phone number: ").strip()
    if not phone.isdigit():
        print("Phone number must contain only digits.")
        return

    email = input("Enter email address: ").strip()
    if "@" not in email or "." not in email:
        print("Invalid email format.")
        return

    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print("Contact added successfully.")

def search_contact(contacts):
    """Search for a contact by name."""
    search_name = input("Enter name to search: ").strip().lower()
    found = False
    for contact in contacts:
        if contact["name"].lower() == search_name:
            print(f"\nName : {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            found = True
    if not found:
        print("Contact not found.")

def update_contact(contacts):
    """Update an existing contact."""
    name_to_update = input("Enter the name of the contact to update: ").strip().lower()
    for contact in contacts:
        if contact["name"].lower() == name_to_update:
            print("Leave the field empty if you don't want to change it.")
            new_name = input(f"New name [{contact['name']}]: ").strip()
            new_phone = input(f"New phone [{contact['phone']}]: ").strip()
            new_email = input(f"New email [{contact['email']}]: ").strip()

            if new_name:
                contact['name'] = new_name
            if new_phone and new_phone.isdigit():
                contact['phone'] = new_phone
            elif new_phone:
                print("Invalid phone. Must be digits only.")
            if new_email and "@" in new_email and "." in new_email:
                contact['email'] = new_email
            elif new_email:
                print("Invalid email format.")

            save_contacts(contacts)
            print("Contact updated successfully.")
            return
    print("Contact not found.")

def display_menu():
    print("\n=== Contact Management System ===")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Exit")

def main():
    contacts = load_contacts()

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            search_contact(contacts)
        elif choice == '3':
            update_contact(contacts)
        elif choice == '4':
            print("Exiting Contact Management System.")
            break
        else:
            print("Invalid choice. Please select between 1 and 4.")

if __name__ == "__main__":
    main()
