class Item:
    def __init__(self, name, price, quantity):
        print(f"i bought: {name} and it's total price is:")
        self.price = price
        self.quantity = quantity
        self.name = name

    def total_price(self):
        total_price = self.price * self.quantity
        return total_price
    
item1 = Item("phone", 100, 5)

item1 = Item("laptop", 1000, 4)
