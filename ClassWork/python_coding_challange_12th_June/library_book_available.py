""" Problem 6: Library Book Availability System 
Problem Statement 
The number of available copies of books in a library is stored below. 
Sample Data 
books = { 
    "Python": 5, 
    "Java": 2, 
    "DBMS": 4, 
    "Networking": 1, 
    "OS": 3, 
    "AI": 6, 
    "ML": 2, 
    "Cloud": 5, 
    "Cyber Security": 1, 
    "Web Development": 4 
} 
Tasks 
1. Display books with fewer than 3 copies.  
2. Find the book with maximum copies.  
3. Find the book with minimum copies.  
4. Count total books available.  
5. Generate a restocking list.  """


#Given Data
books = {
    "Python": 5,
    "Java": 2,
    "DBMS": 4,
    "Networking": 1,
    "OS": 3,
    "AI": 6,
    "ML": 2,
    "Cloud": 5,
    "Cyber Security": 1,
    "Web Development": 4
}

# 1. Books with fewer than 3 copies
print("Books with fewer than 3 copies:")
for book, copies in books.items():
    if copies < 3:
        print(book)

# 2. Book with maximum copies (without max)
max_book = ""
max_copies = -1

for book, copies in books.items():
    if copies > max_copies:
        max_copies = copies
        max_book = book

print("\nMaximum copies book:", max_book, max_copies)

# 3. Book with minimum copies (without min)
min_book = ""
min_copies = 999

for book, copies in books.items():
    if copies < min_copies:
        min_copies = copies
        min_book = book

print("\nMinimum copies book:", min_book, min_copies)

# 4. Total books available
total = 0
for copies in books.values():
    total += copies

print("\nTotal books available:", total)

# 5. Restocking list (very low stock)
restocking=[]
print("\nRestocking list:")
for book, copies in books.items():
    if copies <= 2:
        restocking.append(book)

print(restocking)        


""" output:

Books with fewer than 3 copies:
Java
Networking
ML
Cyber Security

Maximum copies book: AI 6

Minimum copies book: Networking 1

Total books available: 33

Restocking list:
['Java', 'Networking', 'ML', 'Cyber Security'] """
