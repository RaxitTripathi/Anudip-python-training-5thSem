""" 5. Library Book Availability 
Sample Data 
books = { 
    "Python Basics": 5, 
    "Data Structures": 0, 
    "Machine Learning": 3, 
    "Java Programming": 2, 
    "DBMS": 0, 
    "Operating Systems": 6, 
    "Networking": 4, 
    "Cloud Computing": 1, 
    "Cyber Security": 0, 
    "Web Development": 7 
} 
Tasks 
• Display books that are currently unavailable.  
• Count the number of available books.  
• Find the book with the maximum copies.  
• Create a list of books having less than 3 copies.  
• Calculate the total number of books available.  """


books = {
    "Python Basics": 5,
    "Data Structures": 0,
    "Machine Learning": 3,
    "Java Programming": 2,
    "DBMS": 0,
    "Operating Systems": 6,
    "Networking": 4,
    "Cloud Computing": 1,
    "Cyber Security": 0,
    "Web Development": 7
}

# Display books that are currently unavailable
print("Unavailable Books:")
for book, copies in books.items():
    if copies == 0:
        print(book)

# Count the number of available books
count = 0
for copies in books.values():
    if copies > 0:
        count += 1

print("\nNumber of available books:", count)

# Find the book with the maximum copies
max_book = max(books, key=books.get)
print("\nBook with maximum copies:", max_book)
print("Copies:", books[max_book])

# Create a list of books having less than 3 copies
low_stock = []
for book, copies in books.items():
    if copies < 3:
        low_stock.append(book)

print("\nBooks having less than 3 copies:")
print(low_stock)

# Calculate the total number of books available
total_books = 0

for copies in books.values():
    total_books += copies

print("\nTotal number of books available:", total_books)