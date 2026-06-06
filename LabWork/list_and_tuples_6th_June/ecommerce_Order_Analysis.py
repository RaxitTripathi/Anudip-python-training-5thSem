'''Problem Statement 
An online store records orders as: 
orders = [ 
    ("Laptop", 55000), 
    ("Mouse", 800), 
    ("Keyboard", 1500), 
    ("Monitor", 12000), 
    ("Pen Drive", 600) 
] 
Write a program to: 
• Display all products costing more than ₹1000.  
• Find the most expensive product.  
• Calculate the total order value.  
• Count products costing below ₹1000. '''

orders = [ 
    ("Laptop", 55000), 
    ("Mouse", 800), 
    ("Keyboard", 1500), 
    ("Monitor", 12000), 
    ("Pen Drive", 600) 
] 

#Display all products costing more than ₹1000. 

print("Products costing more than ₹1000:")
for product in orders:
    if(product[1] > 1000):
        print(product[0],product[1])


# Find the most expensive product

print("\nExpensive Product:")
expensive_product=orders[0]
for product in orders:
    if(product[1] > expensive_product[1]):
        expensive_product=product
print(expensive_product[0],expensive_product[1])

# Calculate the total order value
total_order_value=0
for product in orders:
    total_order_value += product[1]
print("\nTotal order value:",total_order_value)    

# Count products costing below ₹1000

count_product=0
for product in orders:
    if product[1] < 1000:
        count_product += 1
print("\nProducts costing below ₹1000:",count_product)        