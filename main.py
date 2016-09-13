
class Contact:
    all_contacts = []

    def __init__(self, name, email):
        self.name = name
        self.email = email

    @classmethod
    def reset_contacts(cls):
        cls.all_contacts = []


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
print(Supplier.all_orders)


class ContactList(list):
    pass
