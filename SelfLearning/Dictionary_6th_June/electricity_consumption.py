""" 10. Electricity Consumption Report 
Sample Data 
units = { 
    "House101": 320, 
    "House102": 180, 
    "House103": 450, 
    "House104": 290, 
    "House105": 150, 
    "House106": 510, 
    "House107": 220, 
    "House108": 390, 
    "House109": 170, 
    "House110": 260 
} 
Tasks 
• Display houses consuming more than 300 units.  
• Count houses consuming less than 200 units.  
• Find the house with the highest consumption.  
• Create a list of houses eligible for an energy-saving awareness campaign (consumption > 400 units).  
• Categorize houses as:  
o Low: < 200 units  
o Medium: 200–350 units  
o High: > 350 units   """

units = {
    "House101": 320,
    "House102": 180,
    "House103": 450,
    "House104": 290,
    "House105": 150,
    "House106": 510,
    "House107": 220,
    "House108": 390,
    "House109": 170,
    "House110": 260
}

# Display houses consuming more than 300 units
print("Houses consuming more than 300 units:")
for house, unit in units.items(): # units.items() → gives key + value pairs
    if unit > 300:
        print(house, ":", unit)

# Count houses consuming less than 200 units
count = 0
for unit in units.values(): #returns all the values only from the dictionary.
    if unit < 200:
        count += 1

print("\nHouses consuming less than 200 units:", count)

# Find the house with the highest consumption
highest_house = ""
highest_units = 0

for house, unit in units.items():  # units.items() → gives key + value pairs
    if unit > highest_units:
        highest_units = unit
        highest_house = house

print("House with highest consumption:", highest_house)
print("Units Consumed:", highest_units)

# Create a list of houses eligible for awareness campaign
campaign_list = []

for house, unit in units.items():
    if unit > 400:
        campaign_list.append(house)

print("\nHouses eligible for awareness campaign:")
print(campaign_list)

# Categorize houses
print("\nHouse Categories:")

for house, unit in units.items():
    if unit < 200:
        category = "Low"
    elif 200 <= unit <= 350:
        category = "Medium"
    else:
        category = "High"

    print(house, ":", category)