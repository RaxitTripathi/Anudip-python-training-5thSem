""" 2. Inventory Management System 
Sample Data 
inventory = { 
    "Notebook": 45, 
    "Pen": 120, 
    "Pencil": 80, 
    "Eraser": 25, 
    "Marker": 15, 
    "Stapler": 8, 
    "Glue": 12, 
    "Scale": 30, 
    "Folder": 5, 
    "Calculator": 3 
} 
Tasks 
• Display products with stock less than 10.  
• Count products having stock more than 50.  
• Find the product with the minimum stock.  
• Create a list of products that require restocking (stock < 20).  
• Calculate the total inventory count.  """

inventory = {
    "Notebook": 45,
    "Pen": 120,
    "Pencil": 80,
    "Eraser": 25,
    "Marker": 15,
    "Stapler": 8,
    "Glue": 12,
    "Scale": 30,
    "Folder": 5,
    "Calculator": 3
}

# Products with stock less than 10
print("Products with stock less than 10:")
for product, stock in inventory.items():
    if stock < 10:
        print(product, ":", stock)

# Count products having stock more than 50
count = 0
for stock in inventory.values():
    if stock > 50:
        count += 1
print("\nNumber of products with stock more than 50:", count)

# Product with minimum stock
min_product = None
min_quantity = 9999

for product in inventory:
    if inventory[product] < min_quantity:
        min_quantity = inventory[product]
        min_product = product

print("Product with minimum stock:", min_product)
print("Quantity:", min_quantity)

# Products that require restocking (stock < 20)
restock = []
for product, stock in inventory.items():
    if stock < 20:
        restock.append(product)
print("\nProducts requiring restocking:", restock)

# Total inventory count
total_stock = 0

for stock in inventory.values():
    total_stock += stock

print("\nTotal inventory count:", total_stock)