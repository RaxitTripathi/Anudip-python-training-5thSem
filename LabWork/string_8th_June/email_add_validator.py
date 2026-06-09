""" 6. Chat Message Analytics 
Problem Statement 
A user enters an email address: 
rahul.sharma2026@gmail.com 
Tasks 
Write a program to: 
1. Extract username.  
2. Extract domain name.  
3. Extract extension.  
4. Count digits present in username.  
5. Count special characters.  
6. Check whether:  
o Exactly one '@' exists.  
o At least one '.' exists after '@'.  
7. Display Valid Email or Invalid Email.  """



email = "rahul.sharma2026@gmail.com"

# 1. Check exactly one '@'
at_count = 0

for ch in email:
    if ch == "@":
        at_count += 1

# 2. Split email into username and domain
if at_count == 1:
    username = email[0:email.index("@")]
    domain = email[email.index("@") + 1:]
else:
    username = ""
    domain = ""

# 3. Extract extension (part after last '.')
if "." in domain:
    extension = domain[domain.rindex(".") + 1:]
else:
    extension = ""

# 4. Count digits in username
digit_count = 0

for ch in username:
    if ch.isdigit():
        digit_count += 1

# 5. Count special characters in username
special_count = 0

for ch in username:
    if not ch.isalnum():
        special_count += 1

# 6. Check '.' exists after '@'
dot_after_at = False

for ch in domain:
    if ch == ".":
        dot_after_at = True

# 7. Display username, domain, extension
print("Username:", username)
print("Domain:", domain)
print("Extension:", extension)

print("Digits in Username:", digit_count)
print("Special Characters in Username:", special_count)

# 8. Email validation
if at_count == 1 and dot_after_at and username != "" and extension != "":
    print("Email Status: Valid Email")
else:
    print("Email Status: Invalid Email")


""" output:

Username: rahul.sharma2026
Domain: gmail.com
Extension: com
Digits in Username: 4
Special Characters in Username: 1
Email Status: Valid Email """