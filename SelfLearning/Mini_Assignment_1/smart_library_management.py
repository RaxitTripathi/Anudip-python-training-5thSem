""" 3. Smart Library Management System 
Problem Statement 
Create a digital library management system. 
Example Structure 
library = { 
    "B101": { 
        "title": "Python Basics", 
        "author": "ABC", 
        "copies": 5 
    } 
} 
Maintain records of at least 30 books. 
Requirements 
1. Add a book.  
2. Remove a book.  
3. Search a book by ID.  
4. Search by title.  
5. Update available copies.  
6. Issue a book.  
7. Return a book.  
8. Display books with fewer than 3 copies.  
9. Display books that are unavailable.  
10. Find the most available book.  
11. Generate a restocking report.  
12. Create a separate dictionary of books requiring immediate purchase.  """


from smart_library_operation import *

library = {}

# 1. Input 30 books
print("Enter details of 30 books:\n")

for i in range(30):
    print(f"\nBook {i+1}")

    bid = input("Enter Book ID: ")
    title = input("Enter Title: ")
    author = input("Enter Author: ")
    copies = int(input("Enter Copies: "))

    library[bid] = {
        "title": title,
        "author": author,
        "copies": copies
    }

print("\nAll 30 books added successfully!")


# 2. Menu system
while True:

    print("\n----- LIBRARY MENU -----")
    print("1. Display books")
    print("2. Add book")
    print("3. Remove book")
    print("4. Search by ID")
    print("5. Search by title")
    print("6. Update copies")
    print("7. Issue book")
    print("8. Return book")
    print("9. Low stock books")
    print("10. Unavailable books")
    print("11. Most available book")
    print("12. Restocking report")
    print("13. Immediate purchase list")
    print("14. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        display_books(library)

    elif choice == "2":
        bid = input("Enter Book ID: ")
        add_book(bid, library)

    elif choice == "3":
        bid = input("Enter Book ID: ")
        remove_book(bid, library)

    elif choice == "4":
        bid = input("Enter Book ID: ")
        search_by_id(bid, library)

    elif choice == "5":
        title = input("Enter Title: ")
        search_by_title(title, library)

    elif choice == "6":
        bid = input("Enter Book ID: ")
        update_copies(bid, library)

    elif choice == "7":
        bid = input("Enter Book ID: ")
        issue_book(bid, library)

    elif choice == "8":
        bid = input("Enter Book ID: ")
        return_book(bid, library)

    elif choice == "9":
        low_stock_books(library)

    elif choice == "10":
        unavailable_books(library)

    elif choice == "11":
        most_available(library)

    elif choice == "12":
        restocking_report(library)

    elif choice == "13":
        immediate_purchase(library)

    elif choice == "14":
        print("Exiting...")
        break

    else:
        print("Invalid choice")