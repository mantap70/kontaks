class ContactView:
    @staticmethod
    def display_contacts(contacts):
        if not contacts:
            print("No contacts available.")
            return
        print(f"{'No.':<5}{'Name':<20}{'Phone':<15}{'Email'}")
        print("=" * 50)
        for idx, contact in enumerate(contacts, 1):
            print(f"{idx:<5}{contact.name:<20}{contact.phone:<15}{contact.email}")
        print("=" * 50)

    @staticmethod
    def display_message(message):
        print(message)