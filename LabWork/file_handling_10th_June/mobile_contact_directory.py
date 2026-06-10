""" 4. Mobile Contact Directory System 
Problem Statement 
Contacts are stored in contacts.txt. 
File Format 
Anuj,9876543210 
Rahul,9876543211 
Priya,9876543212 
Neha,9876543213 
Amit,9876543214 
Sneha,9876543215 
Karan,9876543216 
Pooja,9876543217 
Rohit,9876543218 
Anjali,9876543219 
Requirements 
Create a menu-driven application to: 
1. Display all contacts.  
2. Search a contact by name.  
3. Add a new contact.  
4. Update an existing contact number.  
5. Delete a contact.  
6. Display contacts whose names start with a vowel.  
7. Save all modifications back to the file.  """

# Mobile Contact Directory System


# Display all contacts
def display_contacts():

    file = open("contacts.txt", "r")
    data = file.read()
    file.close()

    print("\n--- Contact List ---")
    print(data)


# Search a contact by name
def search_contact():

    name = input("Enter Name: ")

    file = open("contacts.txt", "r")
    data = file.read()
    file.close()

    contacts = data.split("\n")

    found = False

    for contact in contacts:

        details = contact.split(",")

        if details[0].lower() == name.lower():

            print("\nContact Found")
            print("Name :", details[0])
            print("Number :", details[1])

            found = True
            break

    if not found:
        print("Contact not found")


# Add a new contact
def add_contact():

    name = input("Enter Name: ")
    number = input("Enter Mobile Number: ")

    file = open("contacts.txt", "r")
    data = file.read()
    file.close()

    data += "\n" + name + "," + number

    file = open("contacts.txt", "w")
    file.write(data)
    file.close()

    print("Contact added successfully")


# Update an existing contact number
def update_contact():

    name = input("Enter Name to Update: ")

    file = open("contacts.txt", "r")
    data = file.read()
    file.close()

    contacts = data.split("\n")

    found = False

    for i in range(len(contacts)):

        details = contacts[i].split(",")

        if details[0].lower() == name.lower():

            new_number = input("Enter New Number: ")

            details[1] = new_number

            contacts[i] = ",".join(details)

            found = True

            print("Contact updated successfully")
            break

    if found:

        new_data = "\n".join(contacts)

        file = open("contacts.txt", "w")
        file.write(new_data)
        file.close()

    else:
        print("Contact not found")


# Delete a contact
def delete_contact():

    name = input("Enter Name to Delete: ")

    file = open("contacts.txt", "r")
    data = file.read()
    file.close()

    contacts = data.split("\n")

    new_contacts = []

    found = False

    for contact in contacts:

        details = contact.split(",")

        if details[0].lower() == name.lower():
            found = True
        else:
            new_contacts.append(contact)

    if found:

        new_data = "\n".join(new_contacts)

        file = open("contacts.txt", "w")
        file.write(new_data)
        file.close()

        print("Contact deleted successfully")

    else:
        print("Contact not found")


# Display contacts whose names start with a vowel
def vowel_contacts():

    file = open("contacts.txt", "r")
    data = file.read()
    file.close()

    contacts = data.split("\n")

    print("\n--- Contacts Starting With Vowel ---")

    for contact in contacts:

        details = contact.split(",")

        if details[0][0].lower() in "aeiou":
            print(contact)


# Menu driven program
while True:

    print("\n===== Mobile Contact Directory System =====")
    print("1. Display All Contacts")
    print("2. Search Contact")
    print("3. Add Contact")
    print("4. Update Contact Number")
    print("5. Delete Contact")
    print("6. Display Contacts Starting With Vowel")
    print("7. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        display_contacts()

    elif choice == "2":
        search_contact()

    elif choice == "3":
        add_contact()

    elif choice == "4":
        update_contact()

    elif choice == "5":
        delete_contact()

    elif choice == "6":
        vowel_contacts()

    elif choice == "7":
        print("Thank You")
        break

    else:
        print("Invalid Choice")