""" Problem 1: Cyber Security Login Audit System 
Problem Statement 
A file named login_logs.txt contains user login attempts in the following format: 
username,status 
anuj,Success 
rahul,Failed 
anuj,Failed 
priya,Failed 
rahul,Failed 
neha,Success 
anuj,Failed 
karan,Failed 
rahul,Success 
priya,Failed 
Tasks 
1. Count successful and failed login attempts.  
2. Identify users with more than 2 failed attempts.  
3. Create a dictionary storing the number of failures per user.  
4. Create a set of users who logged in successfully.  
5. Display users whose accounts should be reviewed.  """

def login_audit(filename):

    success_count = 0
    failed_count = 0

    failure_dict = {}
    successful_users = set()

    with open(filename, "r") as file:

        for line in file:
            line = line.strip()

            if line == "username,status":
                continue

            username, status = line.split(",")

            if status == "Success":
                success_count += 1
                successful_users.add(username)

            elif status == "Failed":
                failed_count += 1

                if username in failure_dict:
                    failure_dict[username] += 1
                else:
                    failure_dict[username] = 1

    print("Successful Login Attempts:", success_count)
    print("Failed Login Attempts:", failed_count)

    print("\nFailures Per User:")
    for user, count in failure_dict.items():
        print(user, ":", count)

    print("\nUsers Logged In Successfully:")
    print(successful_users)

    print("\nAccounts To Be Reviewed:")
    for user, count in failure_dict.items():
        if count > 2:
            print(user)


try:
    login_audit("login_logs.txt")

except FileNotFoundError:
    print("Error: File not found.")

except Exception as e:
    print("Error:", e)