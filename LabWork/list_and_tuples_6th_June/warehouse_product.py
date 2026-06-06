'''9. Warehouse Product Inspection 
Problem Statement 
Product IDs and quality status: 
products = [ 
    (101, "Pass"), 
    (102, "Fail"), 
    (103, "Pass"), 
    (104, "Fail"), 
    (105, "Pass") 
] 
Write a program to: 
• Display failed product IDs.  
• Count passed and failed products.  
• Calculate pass percentage.  
• Stop checking if 3 failures are found.'''

products = [ 
    (101, "Pass"), 
    (102, "Fail"), 
    (103, "Pass"), 
    (104, "Fail"), 
    (105, "Pass") 
] 

# Display failed product IDs

print("Failed products IDs")
for product in products:
    if(product[1] == "Fail"):
        print(product[0])

# Count passed and failed products   
count_pass=0
count_fail=0
for product in products:
    if(product[1] == "Fail"):
        count_fail += 1  
    else:
        count_pass += 1

print("\nPassed products:",count_pass)
print("Failed products:",count_fail)


# Calculate pass percentage
pass_percentage=(count_pass/len(products))*100
print("\nPass percentage:",pass_percentage)

# Stop checking if 3 failures are found.
print()
failure_count = 0

for product in products:
    print("Checking Product ID:", product[0])

    if product[1] == "Fail":
        failure_count += 1

    if failure_count == 3:
        print("3 failures found. Stopping inspection.")
        break