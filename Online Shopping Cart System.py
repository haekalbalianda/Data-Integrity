class CartItem:
    def __init__(self, name, price, quantity):
        self.name = str(name)
        self.price = float(price)
        self.quantity = int(quantity)
    
    def get_total_price(self):
        return self.price * self.quantity
        

class ShoppingCart:
    def __init__(self):
        self.items = []
        
    def add_item(self, item):
        self.items.append(item)
        return f"{item.name} added to the shopping cart."
        
    def remove_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                return f"{item_name} removed from the shopping cart."
        return f"{item_name} not found in the shopping cart."
                
    def get_cart_total(self):
        total = sum(item.get_total_price() for item in self.items)
        return round(total, 2)
                
# Creating a shopping cart object
cart = ShoppingCart()

# Display the initial items
print(f"Initial items: {cart.items}\n")

# Creating some cart items
item1 = CartItem(name="Laptop", price=999.99, quantity=1)
item2 = CartItem(name="Headphones", price=199.99, quantity=2)

# Adding items to the cart
add_item_message_1 = cart.add_item(item1)
print(add_item_message_1) 

add_item_message_2 = cart.add_item(item2)
print(add_item_message_2) 

# Getting total prices for items
total_price_item1 = item1.get_total_price()
print(f"Total price of {item1.name}: {total_price_item1}\n")

total_price_item2 = item2.get_total_price()
print(f"Total price of {item2.name}: {total_price_item2}\n")

# Getting the total cost of the cart
total_cost = cart.get_cart_total()
print(f"Total cost of the cart: {total_cost}\n")            

# Removing an item from the cart
removal_message = cart.remove_item("Headphones")
print(removal_message) 

# Getting the total cost of the cart again
total_cost = cart.get_cart_total()
print(f"Total cost of the cart after removal: {total_cost}\n")
