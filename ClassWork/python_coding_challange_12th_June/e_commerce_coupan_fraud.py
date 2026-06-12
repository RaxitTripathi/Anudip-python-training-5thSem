""" Problem 3: E-Commerce Coupon Fraud Detection 
Problem Statement 
A file named coupons.txt contains coupon usage records. 
SAVE50 
WELCOME20 
SAVE50 
FESTIVE10 
SAVE50 
WELCOME20 
NEWUSER 
FESTIVE10 
SAVE50 
NEWUSER 
Tasks 
1. Count the usage frequency of each coupon.  
2. Identify coupons used more than 3 times.  
3. Create a set of unique coupons.  
4. Display the most frequently used coupon.  
5. Save suspicious coupon records into fraud_report.txt.  """

def coupon_fraud_detection(filename):

    frequency = {}
    unique_coupons = set()

    with open(filename, "r") as file:

        for line in file:
            coupon = line.strip()

            unique_coupons.add(coupon)

            if coupon in frequency:
                frequency[coupon] += 1
            else:
                frequency[coupon] = 1

    print("Coupon Usage Frequency:")
    for coupon, count in frequency.items():
        print(coupon, ":", count)

    print("\nCoupons Used More Than 3 Times:")
    suspicious = []

    for coupon, count in frequency.items():
        if count > 3:
            print(coupon)
            suspicious.append(coupon)

    print("\nUnique Coupons:")
    print(unique_coupons)

    # Most frequently used coupon
    max_count = 0
    most_used = ""

    for coupon, count in frequency.items():
        if count > max_count:
            max_count = count
            most_used = coupon

    print("\nMost Frequently Used Coupon:", most_used)
    print("Usage Count:", max_count)

    # Save suspicious coupons
    with open("fraud_report.txt", "w") as report:
        report.write("Suspicious Coupons:\n")

        for coupon in suspicious:
            report.write(coupon + "\n")

    print("\nFraud report saved successfully.")


try:
    coupon_fraud_detection("coupons.txt")

except FileNotFoundError:
    print("Error: coupons.txt file not found.")

except Exception as e:
    print("Error:", e)