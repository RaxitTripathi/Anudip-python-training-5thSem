""" Problem 3: Food Delivery Performance Dashboard 
Problem Statement 
Delivery times (in minutes) for different orders are recorded below: 
Sample Data 
delivery_times = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18] 
Tasks 
1. Find the fastest delivery time.  
2. Find the slowest delivery time.  
3. Calculate the average delivery time.  
4. Display delayed orders (>45 minutes).  
5. Categorize deliveries:  
o Fast (≤30 minutes)  
o Normal (31–45 minutes)  
o Delayed (>45 minutes)  """


delivery_times = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18] 

# 1. Find the fastest delivery time. 

fastest_delivery=float("inf")
slowest_delivery=0
avg_delivery=0

for time in delivery_times:
    if time < fastest_delivery:
        fastest_delivery =time
    elif time >slowest_delivery:
        slowest_delivery =time 
    avg_delivery +=time

""" 1. Find the fastest delivery time.  
2. Find the slowest delivery time.  
3. Calculate the average delivery time.    """     

print("Fastest Delivery:",fastest_delivery," minutes")
print("\nSlowest Delivery:",slowest_delivery," minutes")
print("\nAverage Delivery:",avg_delivery/len(delivery_times)," minutes")

# 4. Display delayed orders (>45 minutes). 
delayed_delivery=[]
fast=0
normal=0
delayed=0
print("Delayed Orders:")
for time in delivery_times:
    if time >45:
        delayed_delivery.append(time)
    if time <=30:
        fast +=1
    elif time >=31 and time <=45:
        normal +=1
    else:
        delayed +=1       


print("\nDelayed Orders:")
print(delayed_delivery)

""" 5. Categorize deliveries:  
o Fast (≤30 minutes)  
o Normal (31–45 minutes)  
o Delayed (>45 minutes)  """

print("\nFast delivery:",fast)
print("Normal delivery:",normal)
print("Delayed Delivery:",delayed)


""" output:

Fastest Delivery: 18  minutes

Slowest Delivery: 80  minutes

Average Delivery: 40.8  minutes
Delayed Orders:

Delayed Orders:
[60, 80, 55]

Fast delivery: 4
Normal delivery: 3
Delayed Delivery: 3 """