""" 
2. E-Commerce Inventory & Sales Dashboard 
Problem Statement 
An online store wants to manage products and sales. 
Example Structure 
products = { 
    "P101": { 
        "name": "Laptop", 
        "price": 55000, 
        "stock": 12, 
        "sold": 25 
    } 
} 
Maintain records of at least 30 products. 
Requirements 
1. Display all products.  
2. Add a new product.  
3. Update stock after sales.  
4. Find out-of-stock products.  
5. Find products with stock less than 5.  
6. Calculate total inventory value.  
7. Find best-selling product.  
8. Find least-selling product.  
9. Calculate total revenue generated.  
10. Generate a low-stock report.  
11. Display products whose sales exceed the average sales.  
12. Create a dictionary of products eligible for promotion (sales < 10).  
Challenge 
Generate a complete business report. 
 """

from e_commerce_inventory_operations import *

# dictionary to store products
products = {}

# 1. Input 30 products
print("Enter details of 30 products:\n")

for i in range(30):
    print(f"\nProduct {i+1}")

    pid = input("Enter Product ID: ")
    name = input("Enter Name: ")
    price = float(input("Enter Price: "))
    stock = int(input("Enter Stock: "))
    sold = int(input("Enter Sold: "))

    products[pid] = {
        "name": name,
        "price": price,
        "stock": stock,
        "sold": sold
    }

print("\nAll 30 products added successfully!")


# 2. Menu system
while True:

    print("\n----- INVENTORY MENU -----")
    print("1. Display all products")
    print("2. Add product")
    print("3. Update stock after sales")
    print("4. Out of stock products")
    print("5. Low stock products")
    print("6. Inventory value")
    print("7. Best selling product")
    print("8. Least selling product")
    print("9. Total revenue")
    print("10. Low stock report")
    print("11. Above average sales")
    print("12. Promotion products")
    print("13. Exit")

    choice = input("Enter choice: ")

    # 1. Display
    if choice == "1":
        display_products(products)

    # 2. Add product
    elif choice == "2":
        pid = input("Enter Product ID: ")
        add_product(pid, products)

    # 3. Update stock
    elif choice == "3":
        pid = input("Enter Product ID: ")
        update_stock(pid, products)

    # 4. Out of stock
    elif choice == "4":
        out_of_stock(products)

    # 5. Low stock
    elif choice == "5":
        low_stock(products)

    # 6. Inventory value
    elif choice == "6":
        inventory_value(products)

    # 7. Best seller
    elif choice == "7":
        best_selling(products)

    # 8. Least seller
    elif choice == "8":
        least_selling(products)

    # 9. Revenue
    elif choice == "9":
        total_revenue(products)

    # 10. Low stock report
    elif choice == "10":
        low_stock_report(products)

    # 11. Above average sales
    elif choice == "11":
        above_avg_sales(products)

    # 12. Promotion products
    elif choice == "12":
        promotion_products(products)

    # 13. Exit
    elif choice == "13":
        print("Exiting program...")
        break

    else:
        print("Invalid choice")