""" Problem 17: Daily Sales Performance Analyzer 
Problem Statement 
Daily sales figures (in ₹) for 10 days are stored in a list. 
Sample Data 
sales = [15000, 22000, 18000, 25000, 30000, 17000, 28000, 26000, 21000, 19000] 
Tasks 
1. Find the highest sales.  
2. Find the lowest sales.  
3. Calculate average sales.  
4. Count days with sales above ₹20,000.  
5. Display sales figures below average.  """


def analyze_sales(sales):

    highest = sales[0]
    lowest = sales[0]
    total = 0
    above_20000 = 0

    for sale in sales:
        if sale > highest:
            highest = sale

        if sale < lowest:
            lowest = sale

        total += sale

        if sale > 20000:
            above_20000 += 1

    average = total / len(sales)

    below_average = []
    for sale in sales:
        if sale < average:
            below_average.append(sale)

    print("Highest Sales: ₹", highest)
    print("Lowest Sales: ₹", lowest)
    print("Average Sales: ₹", average)
    print("Days with Sales Above ₹20,000:", above_20000)
    print("Sales Below Average:", below_average)


try:
    sales = [15000, 22000, 18000, 25000, 30000,
             17000, 28000, 26000, 21000, 19000]

    if len(sales) == 0:
        raise ValueError("Sales list cannot be empty")

    analyze_sales(sales)

except ValueError as e:
    print("Error:", e)

except Exception as e:
    print("Unexpected Error:", e)