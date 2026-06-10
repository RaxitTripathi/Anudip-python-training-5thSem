""" 
2. Food Delivery Performance Tracker 
Problem Statement 
Delivery times (in minutes) for different orders are given below: 
delivery_time = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18] 
Requirements 
Create the following functions: 
1. fastest_delivery(times) 
Returns the shortest delivery time. 
2. delayed_orders(times) 
Returns a list of orders taking more than 45 minutes. 
3. average_delivery_time(times) 
Returns the average delivery time. 
4. delivery_category(times) 
Displays order categories: 
• Fast → ≤ 30 minutes  
• Normal → 31–45 minutes  
• Delayed → > 45 minutes  """


# Delivery Time Analysis System

delivery_time = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18]


# 1. Returns the shortest delivery time
def fastest_delivery(times):
    smallest = times[0]

    for i in times:
        if i < smallest:
            smallest = i

    return smallest


# 2. Returns a list of orders taking more than 45 minutes
def delayed_orders(times):
    delayed = []

    for i in times:
        if i > 45:
            delayed.append(i)

    return delayed


# 3. Returns the average delivery time
def average_delivery_time(times):
    total = 0
    count = 0

    for i in times:
        total += i
        count += 1

    return total / count


# 4. Displays order categories
def delivery_category(times):
    for i in times:
        if i <= 30:
            print(i, "-> Fast")
        elif i <= 45:
            print(i, "-> Normal")
        else:
            print(i, "-> Delayed")


# Main Program
print("Fastest Delivery Time:", fastest_delivery(delivery_time), "minutes")
print("Delayed Orders:", delayed_orders(delivery_time))
print("Average Delivery Time:", average_delivery_time(delivery_time))

print("\nDelivery Categories:")
delivery_category(delivery_time)