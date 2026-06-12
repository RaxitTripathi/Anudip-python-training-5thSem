""" Problem 14: Shopping Cart Billing System 
Problem Statement 
The prices of products purchased by a customer are stored in a tuple. 
Sample Data 
prices = (1250, 799, 450, 999, 300, 1500, 650, 250, 850, 1200) 
Tasks 
1. Calculate the total bill amount.  
2. Find the most expensive product.  
3. Find the least expensive product.  
4. Count products costing more than ₹1,000.  
5. Create a list of products eligible for discount (price > ₹800).  """

prices = (1250, 799, 450, 999, 300, 1500, 650, 250, 850, 1200)

# 1. Total Bill Amount
total_bill = 0
for price in prices:
    total_bill += price

print("Total Bill Amount: ₹", total_bill)

# 2. Most Expensive Product
highest = prices[0]

for price in prices:
    if price > highest:
        highest = price

print("Most Expensive Product: ₹", highest)

# 3. Least Expensive Product
lowest = prices[0]

for price in prices:
    if price < lowest:
        lowest = price

print("Least Expensive Product: ₹", lowest)

# 4. Count Products Costing More Than ₹1000
count = 0

for price in prices:
    if price > 1000:
        count += 1

print("Products Costing More Than ₹1000:", count)

# 5. Products Eligible for Discount (Price > ₹800)
discount_products = []

for price in prices:
    if price > 800:
        discount_products.append(price)

print("Products Eligible for Discount:", discount_products)