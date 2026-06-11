""" Problem 8: Smart Water Consumption Monitoring System 
Problem Statement 
Monthly water consumption (in litres) of households is recorded below. 
Sample Data 
water_usage = { 
    "House101": 1800, 
    "House102": 2200, 
    "House103": 3500, 
    "House104": 2800, 
    "House105": 1600, 
    "House106": 4100, 
    "House107": 2400, 
    "House108": 3900, 
    "House109": 1500, 
    "House110": 4500 
} 
Tasks 
1. Display houses consuming more than 3000 litres.  
2. Find the highest and lowest consumers.  
3. Calculate total water consumption.  
4. Categorize houses:  
o Low (<2000 litres)  
o Medium (2000–3500 litres)  
o High (>3500 litres)  
5. Count households eligible for conservation awareness programs (>2500 litres). 
 """

water_usage = {
    "House101": 1800,
    "House102": 2200,
    "House103": 3500,
    "House104": 2800,
    "House105": 1600,
    "House106": 4100,
    "House107": 2400,
    "House108": 3900,
    "House109": 1500,
    "House110": 4500
}

# 1. Houses consuming more than 3000 litres

print("Houses consuming more than 3000 litres:")

for house, usage in water_usage.items():
    if usage > 3000:
        print(house, usage)

# 2. Highest and Lowest Consumers

first = True

for house, usage in water_usage.items():

    if first:
        highest_house = lowest_house = house
        highest_usage = lowest_usage = usage
        first = False

    if usage > highest_usage:
        highest_usage = usage
        highest_house = house

    if usage < lowest_usage:
        lowest_usage = usage
        lowest_house = house

print("\nHighest Consumer:", highest_house, highest_usage)
print("Lowest Consumer:", lowest_house, lowest_usage)

# 3. Total Water Consumption

total = 0

for usage in water_usage.values():
    total += usage

print("\nTotal Water Consumption:", total)

# 4. Categorize Houses

print("\nHouse Categories:")

for house, usage in water_usage.items():

    if usage < 2000:
        category = "Low"

    elif usage <= 3500:
        category = "Medium"

    else:
        category = "High"

    print(house, ":", category)

# 5. Count households eligible for awareness programs

count = 0

for usage in water_usage.values():
    if usage > 2500:
        count += 1

print("\nEligible Households:", count)