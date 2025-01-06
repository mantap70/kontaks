from data import Contact

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email):
        if not phone.isdigit():
            raise ValueError("Phone number must contain only digits.")
        if "@" not in email or "." not in email:
            raise ValueError("Invalid email format.")
        self.contacts.append(Contact(name, phone, email))

    def delete_contact(self, index):
        if index < 1 or index > len(self.contacts):
            raise IndexError("Invalid contact number.")
        del self.contacts[index - 1]

    def search_contact(self, keyword):
        return [contact for contact in self.contacts if keyword.lower() in contact.name.lower()]