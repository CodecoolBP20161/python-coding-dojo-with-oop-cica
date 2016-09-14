class ContactList(list):

    def search(self, x):
        result = []
        for element in self:
            if x == element[0]:
                result.append(element)
        return result

    def longest_name(self):
        max_lenght = 0
        name = None
        for element in self:
            if len(element[0]) > max_lenght:
                max_lenght = len(element[0])
                name = element[0]
        return name


class Contact:
    all_contacts = ContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.all_contacts.append([name, email])

    @classmethod
    def reset_contacts(cls):
        cls.all_contacts = ContactList()


class Supplier(Contact):
    all_orders = {}

    def __init__(self, name, email):
        super(Supplier, self).__init__(name, email)

    def order(self, order_name):
        try:
            self.all_orders[self.email].append(order_name)
        except KeyError:
            self.all_orders[self.email] = [order_name]


jozsi = Supplier("Józsi", "jozsi@jozsi.jozsi")
jozsi.order("kocka")
jozsi.order("paralelogramma")
print(Contact.all_contacts.search("Józsi"))
# print(Supplier.all_orders)
print(Contact.all_contacts.longest_name())
