""" Assignment 2: Email Validation & Domain Analytics System 
Problem Statement 
An organization has collected 20 email addresses from users. 
Create a program to analyze these email addresses. 
Requirements 
For each email: 
1. Extract username.  
2. Extract domain.  
3. Extract extension.  
4. Count digits in username.  
5. Count special characters.  
6. Check if email is valid:  
o Exactly one '@'  
o Contains '.'  
o No spaces  
7. Display invalid emails.  
8. Count emails belonging to each domain.  
Sample Input 
rahul123@gmail.com 
priya@outlook.com 
anuj@company.in 
Challenge 
Generate a domain report: 
gmail.com     -> 8 users 
outlook.com   -> 5 users 
yahoo.com     -> 3 users 
company.in    -> 4 users """

# Email Validation & Domain Analytics System

emails = []

# Input 20 emails
for i in range(20):
    email = input(f"Enter email {i+1}: ")
    emails.append(email)

domain_count = {}
invalid_emails = []

print("\nEMAIL ANALYSIS")
print("-" * 60)

for email in emails:

    # Validation
    valid = True

    if email.count('@') != 1:
        valid = False

    if '.' not in email:
        valid = False

    if ' ' in email:
        valid = False

    if valid:

        username = email.split('@')[0]
        domain_full = email.split('@')[1]

        domain = domain_full.split('.')[0]
        extension = domain_full.split('.')[-1]

        digit_count = 0
        special_count = 0

        for ch in username:
            if ch.isdigit():
                digit_count += 1
            elif not ch.isalpha():
                special_count += 1

        print(f"\nEmail      : {email}")
        print(f"Username   : {username}")
        print(f"Domain     : {domain}")
        print(f"Extension  : {extension}")
        print(f"Digits     : {digit_count}")
        print(f"Special Ch : {special_count}")

        # Domain Report
        if domain_full in domain_count:
            domain_count[domain_full] += 1
        else:
            domain_count[domain_full] = 1

    else:
        invalid_emails.append(email)

# Invalid Emails
print("\n\nINVALID EMAILS")
print("-" * 60)

if len(invalid_emails) == 0:
    print("No invalid emails found.")
else:
    for email in invalid_emails:
        print(email)

# Domain Analytics Report
print("\n\nDOMAIN REPORT")
print("-" * 60)

for domain, count in domain_count.items():
    print(domain, "->", count, "users")