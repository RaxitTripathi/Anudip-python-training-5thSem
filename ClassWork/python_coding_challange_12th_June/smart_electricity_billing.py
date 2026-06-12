""" Problem 1: Smart Electricity Billing System 
Problem Statement 
Monthly electricity consumption (units) of different houses in a residential society is stored as follows: 
Sample Data 
units = { 
    "House101": 320, 
    "House102": 180, 
    "House103": 510, 
    "House104": 275, 
    "House105": 150, 
    "House106": 430, 
    "House107": 220, 
    "House108": 390, 
    "House109": 145, 
    "House110": 600 
} 
Tasks 
1. Display houses consuming more than 400 units.  
2. Find the highest-consuming house.  
3. Find the lowest-consuming house.  
4. Calculate the total units consumed.  
5. Create separate lists for:  
o Low Consumption (< 200)  
o Medium Consumption (200–400)  
o High Consumption (> 400)  
6. Count houses eligible for an energy-saving campaign (consumption > 300).  """


#Given Data
units = { 
    "House101": 320, 
    "House102": 180, 
    "House103": 510, 
    "House104": 275, 
    "House105": 150, 
    "House106": 430, 
    "House107": 220, 
    "House108": 390, 
    "House109": 145, 
    "House110": 600 
} 

# 1. Display houses consuming more than 400 units.
total_units=0
highest_consuming_house=""
lowest_consuming_house=""
highest_count=0
lowest_count=float("inf")
print("House consuming more than 400 units:")
for unit in units:
    if units[unit] >400:
        print(unit)
    if units[unit] > highest_count:
        highest_consuming_house=unit
        highest_count =units[unit] 
    elif units[unit] < lowest_count:
        lowest_consuming_house=unit
        lowest_count=units[unit]  
    total_units +=units[unit]         

# 2. Find the highest-consuming house.
# 3. Find the lowest-consuming house
print("\nHighest Consumption:\n",highest_consuming_house,"(",highest_count,")")
print("Lowest Consumption:\n",lowest_consuming_house,"(",lowest_count,")")

# 4. Calculate the total units consumed.
print("Total Units Consumed:",total_units)

# 5. Create separate lists for:  
# o Low Consumption (< 200)  
# o Medium Consumption (200–400)  
# o High Consumption (> 400)  

low_consumption_200=[]
medium_consumption_200_400=[]
high_consumption_400=[]
count_energy_saving=0
for unit in units:
    if units[unit] < 200:
        low_consumption_200.append(unit)
    elif units[unit] < 400:
        medium_consumption_200_400.append(unit)  
    else:
        high_consumption_400.append(unit)
    if units[unit] > 300:
        count_energy_saving +=1   

print("\nLow Consumption:\n",low_consumption_200)
print("Medium Consumption:\n",medium_consumption_200_400)
print("High Consumtion:\n",high_consumption_400)

# 6. Count houses eligible for an energy-saving campaign (consumption > 300).

print("\nEligible for Energy-Saving Campaign:",count_energy_saving)

""" 
output:

House consuming more than 400 units:
House103
House106
House110

Highest Consumption:
 House110 ( 600 )
Lowest Consumption:
 House109 ( 145 )
Total Units Consumed: 3220

Low Consumption:
 ['House102', 'House105', 'House109']
Medium Consumption:
 ['House101', 'House104', 'House107', 'House108']
High Consumtion:
 ['House103', 'House106', 'House110']

Eligible for Energy-Saving Campaign: 5 """

