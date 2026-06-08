""" 1. Online Shopping Order Analytics 
Problem Statement 
An e-commerce company stores product sales data as: 
sales = { 
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
1. Display products sold more than 20 times.  
2. Find the best-selling product.  
3. Find the least-selling product.  
4. Calculate total products sold.  
5. Create a list of products requiring promotion (sales < 15).  
6. Count products having sales between 10 and 30.   """

#Given data
sales = { 
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

#Display products sold more than 20 times
print("Products Sold More Than 20 Times: ")
for product in sales:
    if(sales[product] > 20):
        print(product)

# 2. Find the best-selling product. 

best_selling_price=0
best_selling_product=None
for product in sales:
    if(sales[product] > best_selling_price):
        best_selling_price=sales[product]
        best_selling_product=product

print("Best Selling Product:",best_selling_product,(best_selling_price))

# 3. Find the least-selling product. 
least_selling_price=float("inf")
least_selling_product=None
for product in sales:
    if(sales[product] < least_selling_price):
        least_selling_price=sales[product]
        least_selling_product=product

print("Least Selling Product:",least_selling_product,(least_selling_price))   


# 4. Calculate total products sold.  
count_total=0
for product in sales:
    count_total +=sales[product]

print("Total Units Sold: ",count_total)    

# 5. Create a list of products requiring promotion (sales < 15).  
promotion_list=[]
for product in sales:
    if(sales[product] < 15):
        promotion_list.append(product)

print("Products Requiring Promotion:\n",promotion_list)    

# 6. Count products having sales between 10 and 30.
count_10_15=0
for product in sales:
    if(sales[product] >10 and sales[product] <30):
        count_10_15 +=1

print("Products Having Sales Between 10 and 30:",count_10_15)




# output:

""" Products Sold More Than 20 Times: 
Mouse 
Keyboard 
Headphones 
Router 
 
Best Selling Product: Mouse (45) 
 
Least Selling Product: Printer (8) 
 
Total Units Sold: 213 
 
Products Requiring Promotion: 
['Monitor', 'Printer', 'Tablet'] 
 
Products Having Sales Between 10 and 30: 6 """