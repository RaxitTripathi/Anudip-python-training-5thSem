""" Problem 5: Online Shopping Cart Analyzer 
Problem Statement 
The prices of products added to a shopping cart are stored below. 
Sample Data 
cart = [1500, 899, 450, 2500, 799, 1200, 300, 650, 1800, 999] 
Tasks 
1. Calculate the total cart value.  
2. Find the most expensive and cheapest products.  
3. Count products eligible for premium shipping (price > ₹1000).  
4. Generate a discount list (products above ₹1500).  
5. Calculate the average product price.   """


# Problem 5: Online Shopping Cart Analyzer

cart = [1500, 899, 450, 2500, 799, 1200, 300, 650, 1800, 999]

# 1. Calculate total cart value
total = sum(cart)

# 2. Find most expensive and cheapest products
most_expensive = max(cart)
cheapest = min(cart)

# 3. Count products eligible for premium shipping (price > 1000)
premium_count = 0
for price in cart:
    if price > 1000:
        premium_count += 1

# 4. Generate discount list (products above 1500)
discount_list = []

for price in cart:
    if price > 1500:
        discount_list.append(price)

# 5. Calculate average product price
average = total / len(cart)

# Display Results
print("Total Cart Value:", total)

print("Most Expensive Product:", most_expensive)
print("Cheapest Product:", cheapest)

print("Products Eligible for Premium Shipping:", premium_count)

print("Discount List:")
for price in discount_list:
    print(price)

print("Average Product Price:", average)

