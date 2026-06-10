
# 1. Display all books
def display_books(library):
    for bid in library:
        print(bid, library[bid])


# 2. Add book
def add_book(bid, library):

    if bid in library:
        print("Book ID already exists")

    else:
        title = input("Enter title: ")
        author = input("Enter author: ")
        copies = int(input("Enter copies: "))

        library[bid] = {
            "title": title,
            "author": author,
            "copies": copies
        }

        print("Book added successfully")


# 3. Remove book
def remove_book(bid, library):

    if bid in library:
        del library[bid]
        print("Book removed")
    else:
        print("Book not found")


# 4. Search by ID
def search_by_id(bid, library):

    if bid in library:
        print(library[bid])
    else:
        print("Book not found")


# 5. Search by title
def search_by_title(title, library):

    found = False

    for bid in library:
        if library[bid]["title"].lower() == title.lower():
            print(bid, library[bid])
            found = True

    if not found:
        print("Book not found")


# 6. Update copies
def update_copies(bid, library):

    if bid in library:
        copies = int(input("Enter new copies: "))
        library[bid]["copies"] = copies
        print("Copies updated")
    else:
        print("Book not found")


# 7. Issue book
def issue_book(bid, library):

    if bid in library:

        if library[bid]["copies"] > 0:
            library[bid]["copies"] -= 1
            print("Book issued")
        else:
            print("No copies available")

    else:
        print("Book not found")


# 8. Return book
def return_book(bid, library):

    if bid in library:
        library[bid]["copies"] += 1
        print("Book returned")
    else:
        print("Book not found")


# 9. Books with < 3 copies
def low_stock_books(library):

    for bid in library:
        if library[bid]["copies"] < 3:
            print(bid, library[bid])


# 10. Unavailable books
def unavailable_books(library):

    for bid in library:
        if library[bid]["copies"] == 0:
            print(bid, library[bid])


# 11. Most available book
def most_available(library):

    best_id = None

    for bid in library:
        if best_id is None or library[bid]["copies"] > library[best_id]["copies"]:
            best_id = bid

    print(best_id, library[best_id])


# 12. Restocking report
def restocking_report(library):

    report = {}

    for bid in library:
        if library[bid]["copies"] < 3:
            report[bid] = library[bid]

    print("Restocking Report")
    for bid in report:
        print(bid, report[bid])


# 13. Immediate purchase list
def immediate_purchase(library):

    urgent = {}

    for bid in library:
        if library[bid]["copies"] == 0:
            urgent[bid] = library[bid]

    print("Immediate Purchase List")
    for bid in urgent:
        print(bid, urgent[bid])