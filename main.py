class Item:
    def __init__(self, name: str, price: float, quantity: int):
        print(f"i bought: {name} and it's total price is:")
        #Run validation to the recieved arguments
        assert price >=0
        assert quantity >=0
        
        # Assign to self object
        self.price = price
        self.quantity = quantity
        self.name = name

    def total_price(self):
        total_price = self.price * self.quantity
        return total_price
    
item1 = Item("phone", 100, 5)

item2 = Item("laptop", 1000, 4)
