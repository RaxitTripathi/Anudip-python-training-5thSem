""" 5. Smart Electricity Billing System 
Problem Statement 
Monthly electricity consumption (units) is stored as: 
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

    Tasks 
1. Display houses consuming more than 400 units.  
2. Find the highest-consuming house.  
3. Find the lowest-consuming house.  
4. Calculate total units consumed.  
5. Create lists:  
o Low Consumption (< 200)  
o Medium Consumption (200–400)  
o High Consumption (> 400)  
6. Count houses eligible for an energy-saving campaign (consumption > 300). 
}  """



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

# 1. Houses consuming more than 400 units
print("Houses Consuming More Than 400 Units:")
for house, unit in units.items():
    if unit > 400:
        print(house, ":", unit)

# 2. Highest-consuming house
highest_house = None
highest_units = 0

for house, unit in units.items():
    if unit > highest_units:
        highest_units = unit
        highest_house = house

print("\nHighest-Consuming House:")
print(highest_house, ":", highest_units)

# 3. Lowest-consuming house
lowest_house = None
lowest_units = float('inf')

for house, unit in units.items():
    if unit < lowest_units:
        lowest_units = unit
        lowest_house = house

print("\nLowest-Consuming House:")
print(lowest_house, ":", lowest_units)

# 4. Calculate total units consumed
total_units = 0

for unit in units.values():
    total_units += unit

print("\nTotal Units Consumed:", total_units)

# 5. Create consumption categories
low_consumption = []
medium_consumption = []
high_consumption = []

for house, unit in units.items():

    if unit < 200:
        low_consumption.append(house)

    elif 200 <= unit <= 400:
        medium_consumption.append(house)

    else:
        high_consumption.append(house)

print("\nLow Consumption (<200):", low_consumption)
print("Medium Consumption (200-400):", medium_consumption)
print("High Consumption (>400):", high_consumption)

# 6. Count houses eligible for energy-saving campaign (consumption > 300).  
count = 0

for unit in units.values():
    if unit > 300:
        count += 1

print("\nHouses Eligible for Energy-Saving Campaign:", count)


""" output:

Houses Consuming More Than 400 Units:
House103 : 510
House106 : 430
House110 : 600

Highest-Consuming House:
House110 : 600

Lowest-Consuming House:
House109 : 145

Total Units Consumed: 3220

Low Consumption (<200): ['House102', 'House105', 'House109']
Medium Consumption (200-400): ['House101', 'House104', 'House107', 'House108']
High Consumption (>400): ['House103', 'House106', 'House110']

Houses Eligible for Energy-Saving Campaign: 5 """
