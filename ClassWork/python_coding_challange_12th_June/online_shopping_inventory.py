""" Problem Statement 
An online store maintains stock quantities of products. 
Sample Data 
inventory = { 
    "Laptop": 15, 
    "Mouse": 45, 
    "Keyboard": 32, 
    "Monitor": 12, 
    "Headphones": 28, 
    "Printer": 8, 
    "Webcam": 20, 
    "Speaker": 18, 
    "Tablet": 10, 
    "Router": 25 
} 
Tasks 
1. Display products with stock below 15 units.  
2. Find the product with maximum stock.  
3. Find the product with minimum stock.  
4. Calculate total stock available.  
5. Create a list of products requiring restocking (<10 units).  """


inventory = {
    "Laptop": 15,
    "Mouse": 45,
    "Keyboard": 32,
    "Monitor": 12,
    "Headphones": 28,
    "Printer": 8,
    "Webcam": 20,
    "Speaker": 18,
    "Tablet": 10,
    "Router": 25
}

# 1. Products with stock below 15
print("Products below 15 units:")
for product, stock in inventory.items():
    if stock < 15:
        print(product, ":", stock)

# 2. Product with maximum stock (without max)
max_product = ""
max_stock = -1

for product, stock in inventory.items():
    if stock > max_stock:
        max_stock = stock
        max_product = product

print("\nMaximum stock product:", max_product, max_stock)

# 3. Product with minimum stock (without min)
min_product = ""
min_stock = 999

for product, stock in inventory.items():
    if stock < min_stock:
        min_stock = stock
        min_product = product

print("\nMinimum stock product:", min_product, min_stock)

# 4. Total stock
total_stock = 0

for stock in inventory.values():
    total_stock += stock

print("\nTotal stock available:", total_stock)

# 5. Restocking list (<10 units)
print("\nProducts needing restock (<10):")
for product, stock in inventory.items():
    if stock < 10:
        print(product)