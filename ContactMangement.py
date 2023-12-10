class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        print("\nContact List:")
        for contact in self.contacts:
            print(f"Name: {contact.name} | Phone: {contact.phone}")

    def search_contact(self, keyword):
        results = [contact for contact in self.contacts
                   if keyword.lower() in contact.name.lower() or keyword in contact.phone]
        return results

    def update_contact(self, old_name, new_contact):
        for i, contact in enumerate(self.contacts):
            if contact.name == old_name:
                self.contacts[i] = new_contact
                print(f"Contact '{old_name}' updated successfully.")
                return True
        print(f"Contact '{old_name}' not found.")
        return False

    def delete_contact(self, name):
        for i, contact in enumerate(self.contacts):
            if contact.name == name:
                del self.contacts[i]
                print(f"Contact '{name}' deleted successfully.")
                return True
        print(f"Contact '{name}' not found.")
        return False

def main():
    contact_manager = ContactManager()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            address = input("Enter address: ")
            new_contact = Contact(name, phone, email, address)
            contact_manager.add_contact(new_contact)
            print("Contact added successfully.")

        elif choice == '2':
            contact_manager.view_contacts()

        elif choice == '3':
            keyword = input("Enter name or phone number to search: ")
            search_results = contact_manager.search_contact(keyword)
            if search_results:
                print("\nSearch Results:")
                for result in search_results:
                    print(f"Name: {result.name} | Phone: {result.phone}")
            else:
                print("No contacts found.")

        elif choice == '4':
            old_name = input("Enter the name of the contact to update: ")
            new_name = input("Enter new name: ")
            new_phone = input("Enter new phone number: ")
            new_email = input("Enter new email address: ")
            new_address = input("Enter new address: ")
            updated_contact = Contact(new_name, new_phone, new_email, new_address)
            contact_manager.update_contact(old_name, updated_contact)

        elif choice == '5':
            name_to_delete = input("Enter the name of the contact to delete: ")
            contact_manager.delete_contact(name_to_delete)

        elif choice == '6':
            print("Exiting Contact Management System.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
