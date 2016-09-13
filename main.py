
class Contact:
    all_contacts = []

    def __init__(self, name, email):
        self.name = name
        self.email = email

    @classmethod
    def reset_contacts(cls):
        cls.all_contacts = []
