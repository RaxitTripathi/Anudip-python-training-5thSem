""" 5. Daily Expense Tracker and Report Generator 
Problem Statement 
Daily expenses are recorded in expenses.txt. 
File Format 
Food,450 
Travel,300 
Shopping,1200 
Electricity,850 
Internet,700 
Entertainment,600 
Medicine,400 
Education,1500 
Fuel,900 
Miscellaneous,250 
Requirements 
Develop a program to: 
1. Display all expenses.  
2. Calculate total expenditure.  
3. Find the category with highest and lowest spending.  
4. Display expenses greater than ₹800.  
5. Add a new expense category.  
6. Update an existing expense amount.  
7. Generate a summary report in report.txt containing:  
o Total Expenses  
o Highest Expense Category  
o Lowest Expense Category  
o Categories spending more than ₹800  """

# Daily Expense Tracker and Report Generator


# Display all expenses
def display_expenses():

    file = open("expenses.txt", "r")
    data = file.read()
    file.close()

    print("\n--- Expense Records ---")
    print(data)


# Calculate total expenditure
def total_expense():

    file = open("expenses.txt", "r")
    data = file.read()
    file.close()

    expenses = data.split("\n")

    total = 0

    for expense in expenses:

        details = expense.split(",")

        total += int(details[1])

    print("\nTotal Expenditure = ₹", total)


# Find highest and lowest spending category
def highest_lowest():

    file = open("expenses.txt", "r")
    data = file.read()
    file.close()

    expenses = data.split("\n")

    highest_category = ""
    highest_amount = -1

    lowest_category = ""
    lowest_amount = 999999

    for expense in expenses:

        details = expense.split(",")

        amount = int(details[1])

        if amount > highest_amount:
            highest_amount = amount
            highest_category = details[0]

        if amount < lowest_amount:
            lowest_amount = amount
            lowest_category = details[0]

    print("\nHighest Expense :", highest_category, "-", highest_amount)
    print("Lowest Expense :", lowest_category, "-", lowest_amount)


# Display expenses greater than ₹800
def expenses_above_800():

    file = open("expenses.txt", "r")
    data = file.read()
    file.close()

    expenses = data.split("\n")

    print("\n--- Expenses Greater Than ₹800 ---")

    for expense in expenses:

        details = expense.split(",")

        if int(details[1]) > 800:
            print(expense)


# Add a new expense category
def add_expense():

    category = input("Enter Category Name: ")
    amount = input("Enter Amount: ")

    file = open("expenses.txt", "r")
    data = file.read()
    file.close()

    data += "\n" + category + "," + amount

    file = open("expenses.txt", "w")
    file.write(data)
    file.close()

    print("Expense added successfully")


# Update an existing expense amount
def update_expense():

    category = input("Enter Category Name: ")

    file = open("expenses.txt", "r")
    data = file.read()
    file.close()

    expenses = data.split("\n")

    found = False

    for i in range(len(expenses)):

        details = expenses[i].split(",")

        if details[0].lower() == category.lower():

            new_amount = input("Enter New Amount: ")

            details[1] = new_amount

            expenses[i] = ",".join(details)

            found = True

            print("Expense updated successfully")
            break

    if found:

        new_data = "\n".join(expenses)

        file = open("expenses.txt", "w")
        file.write(new_data)
        file.close()

    else:
        print("Category not found")


# Generate summary report in report.txt
"""  Total Expenses  
o Highest Expense Category  
o Lowest Expense Category  
o Categories spending more than ₹800   """


def generate_report():

    file = open("expenses.txt", "r")
    data = file.read()
    file.close()

    expenses = data.split("\n")

    total = 0

    highest_category = ""
    highest_amount = -1

    lowest_category = ""
    lowest_amount = 999999

    above_800 = ""

    for expense in expenses:

        details = expense.split(",")

        category = details[0]
        amount = int(details[1])

        total += amount

        if amount > highest_amount:
            highest_amount = amount
            highest_category = category

        if amount < lowest_amount:
            lowest_amount = amount
            lowest_category = category

        if amount > 800:
            above_800 += category + " - ₹" + str(amount) + "\n"

    report = ""
    report += "Total Expenses : ₹" + str(total) + "\n"
    report += "Highest Expense Category : " + highest_category + "\n"
    report += "Lowest Expense Category : " + lowest_category + "\n\n"
    report += "Categories Spending More Than ₹800\n"
    report += above_800

    file = open("report.txt", "w")
    file.write(report)
    file.close()

    print("Report generated successfully")


# Menu driven program
while True:

    print("\n===== Daily Expense Tracker =====")
    print("1. Display All Expenses")
    print("2. Calculate Total Expenditure")
    print("3. Find Highest and Lowest Spending")
    print("4. Display Expenses Greater Than ₹800")
    print("5. Add New Expense Category")
    print("6. Update Expense Amount")
    print("7. Generate Summary Report")
    print("8. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        display_expenses()

    elif choice == "2":
        total_expense()

    elif choice == "3":
        highest_lowest()

    elif choice == "4":
        expenses_above_800()

    elif choice == "5":
        add_expense()

    elif choice == "6":
        update_expense()

    elif choice == "7":
        generate_report()

    elif choice == "8":
        print("Thank You")
        break

    else:
        print("Invalid Choice")