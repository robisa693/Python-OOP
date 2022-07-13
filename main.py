import csv


class Item:
    pay_rate = 0.8  # The pay rate after 20 % discount
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # Run validations of the received arguments
        assert price >= 0, f"Price {price} is not greater or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

        # Assignment to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as file:
            reader = csv.DictReader(file)
            items = list(reader)
        for item in items:
            Item (
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):
        # We will count out the floats that are .0
        # For example: 5.0, 3.0
        if isinstance(num, float):
            return num.is_integer()  # this is_integer is a built-in method for float, can be confusing
        elif isinstance(num, int):
            return True
        else:
            return False

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"


class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations of the received arguments
        assert price >= 0, f"Price {price} is not greater or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

        # Assignment to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)


Phone1 = Phone("jcsPhonev10", 500, 5)
Phone1.broken_phones = 1
Phone2 = Phone("jcsPhonev20", 700, 5)
Phone2.broken_phones = 1
