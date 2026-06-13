""" 6. Shopping Cart Application (Intermediate) 
Problem Statement: 
Create a Product class containing product name, quantity, and price per unit. 
Implement methods to: 
• Calculate total price.  
• Update quantity.  
• Display product details.  """

class Product:

    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def calculate_total_price(self):
        total = self.quantity * self.price
        print("Total Price =", total)

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity
        print("Quantity Updated")

    def display_details(self):
        print("\nProduct Name:", self.name)
        print("Quantity:", self.quantity)
        print("Price per Unit:", self.price)


# Main
name = input("Enter Product Name: ")
quantity = int(input("Enter Quantity: "))
price = float(input("Enter Price per Unit: "))

p1 = Product(name, quantity, price)

p1.display_details()
p1.calculate_total_price()

new_quantity = int(input("\nEnter New Quantity: "))
p1.update_quantity(new_quantity)

p1.display_details()
p1.calculate_total_price()