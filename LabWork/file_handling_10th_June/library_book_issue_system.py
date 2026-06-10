""" 2. Library Book Issue System 
Problem Statement 
A library stores book information in books.txt. 
File Format 
B101,Python Basics,5 
B102,Java Programming,2 
B103,Data Science,0 
B104,DBMS,3 
B105,Machine Learning,1 
B106,Operating Systems,4 
B107,Networking,2 
B108,Cyber Security,6 
B109,Cloud Computing,0 
B110,Web Development,3 
Requirements 
Develop a program to: 
1. Display all books.  
2. Search a book using Book ID.  
3. Issue a book (decrease quantity by 1).  
4. Return a book (increase quantity by 1).  
5. Display unavailable books.  
6. Display books requiring restocking (copies < 2).  
7. Update the file after every issue/return operation."""

# Library Book Issue System

# 1. Display all books. 
def display_books():
    file = open("books.txt", "r")
    data = file.read()
    file.close()

    print("\n--- All Books ---")
    print(data)

# 2. Search a book using Book ID.
def search_book():
    book_id = input("Enter Book ID: ")

    file = open("books.txt", "r")
    data = file.read()
    file.close()

    books = data.split("\n")

    found = False

    for book in books:
        details = book.split(",")

        if details[0] == book_id:
            print("\nBook Found")
            print("Book ID :", details[0])
            print("Title   :", details[1])
            print("Copies  :", details[2])
            found = True
            break

    if not found:
        print("Book not found")

# 3. Issue a book (decrease quantity by 1).
def issue_book():
    book_id = input("Enter Book ID to issue: ")

    file = open("books.txt", "r")
    data = file.read()
    file.close()

    books = data.split("\n")
    new_data = ""

    found = False

    for i in range(len(books)):
        details = books[i].split(",")

        if details[0] == book_id:
            found = True

            qty = int(details[2])

            if qty > 0:
                qty -= 1
                details[2] = str(qty)
                print("Book issued successfully")
            else:
                print("Book unavailable")

        books[i] = ",".join(details)  #joins the list back into a string:

    new_data = "\n".join(books)

    file = open("books.txt", "w")
    file.write(new_data)
    file.close()

    if not found:
        print("Book not found")

# 4. Return a book (increase quantity by 1).
def return_book():
    book_id = input("Enter Book ID to return: ")

    file = open("books.txt", "r")
    data = file.read()
    file.close()

    books = data.split("\n")

    found = False

    for i in range(len(books)):
        details = books[i].split(",")

        if details[0] == book_id:
            found = True

            qty = int(details[2])
            qty += 1
            details[2] = str(qty)

            books[i] = ",".join(details)

            print("Book returned successfully")

    new_data = "\n".join(books)

    file = open("books.txt", "w")
    file.write(new_data)
    file.close()

    if not found:
        print("Book not found")


#5. Display unavailable books.
def unavailable_books():
    file = open("books.txt", "r")
    data = file.read()
    file.close()

    books = data.split("\n")

    print("\n--- Unavailable Books ---")

    for book in books:
        details = book.split(",")

        if int(details[2]) == 0:
            print(book)

#6. Display books requiring restocking (copies < 2). 
def restocking_books():
    file = open("books.txt", "r")
    data = file.read()
    file.close()

    books = data.split("\n")

    print("\n--- Books Requiring Restocking ---")

    for book in books:
        details = book.split(",")

        if int(details[2]) < 2:
            print(book)


#main
while True:
    print("\n===== Library Book Issue System =====")
    print("1. Display All Books")
    print("2. Search Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display Unavailable Books")
    print("6. Display Books Requiring Restocking")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        display_books()

    elif choice == "2":
        search_book()

    elif choice == "3":
        issue_book()

    elif choice == "4":
        return_book()

    elif choice == "5":
        unavailable_books()

    elif choice == "6":
        restocking_books()

    elif choice == "7":
        print("Thank You")
        break

    else:
        print("Invalid Choice")
