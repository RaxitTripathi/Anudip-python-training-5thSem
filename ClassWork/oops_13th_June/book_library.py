""" 5. Book Library System (Intermediate) 
Problem Statement: 
Create a Book class with attributes: 
• Book ID  
• Title  
• Author  
• Availability Status  
Implement methods to: 
• Issue a book.  
• Return a book.  
• Display book details.  
Prevent issuing a book that is already issued. """

class Book:

    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True

    def issue_book(self):
        if self.available:
            self.available = False
            print("Book Issued")
        else:
            print("Book Already Issued")
        print("\n----------------------------------")

    def return_book(self):
        self.available = True
        print("Book Returned")
        print("\n----------------------------------")

    def display_details(self):
        print("\n----------------------------------")
        print("Book ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Available:", self.available)
        print("\n----------------------------------")


book_id = int(input("Enter Book ID: "))

title = input("Enter Book Title: ").strip()
if not title:
    exit("No title")
    

author = input("Enter Author Name: ").strip()
if not author:
    exit('No Author')
    
book = Book(book_id,title,author)

while(True):
    print("""-------Enter your chocie--------------
1• Issue a book.  
2• Return a book.  
3• Display book details.
4• Exit """)
    
    user=int(input("Enter your choice:"))

    if user == 1:
        book.issue_book()

    elif user ==2:
        book.return_book()

    elif user ==3:
        book.display_details()

    elif user ==4:
        print("Exiting")

    else:
        print("Invalid Input")

     #Ask the user if they want to perform another operation
    another_operation=input("Do you want to perform another operation? (yes/no): ")
    if another_operation.lower()!="yes":
        print("Thank you for using our services!")
        break
    print("\n----------------------------------")