""" Problem 10: Smart City Waste Collection Management System 
Problem Statement 
The amount of waste collected (in kilograms) from different sectors of a city is stored below. 
Sample Data 
    "Sector2": 180, 
    "Sector3": 510, 
    "Sector4": 275, 
    "Sector5": 150, 
    "Sector6": 430, 
    "Sector7": 220, 
    "Sector8": 390, 
    "Sector9": 145, 
    "Sector10": 600 
} 
Tasks 
1. Display sectors generating more than 400 kg of waste.  
2. Find the sector generating maximum waste.  
3. Find the sector generating minimum waste.  
4. Calculate the total waste collected.  
5. Categorize sectors:  
o Low Waste (<200 kg)  
o Medium Waste (200–400 kg)  
o High Waste (>400 kg)  
6. Count sectors requiring awareness campaigns (waste generation >300 kg).  
7. Save the awareness campaign list to campaign_sectors.txt.  """


# -----------------------------
# Sample Data (fixed properly)
# -----------------------------
waste = {
    "Sector2": 180,
    "Sector3": 510,
    "Sector4": 275,
    "Sector5": 150,
    "Sector6": 430,
    "Sector7": 220,
    "Sector8": 390,
    "Sector9": 145,
    "Sector10": 600
}

# -----------------------------
# 1. Sectors > 400 kg
# -----------------------------
print("Sectors generating more than 400 kg waste:")
for sector in waste:
    if waste[sector] > 400:
        print(sector, waste[sector])

print("\n")

# -----------------------------
# 2 & 3. Max and Min waste sector (NO max/min)
# -----------------------------
first = True

max_sector = ""
min_sector = ""
max_value = 0
min_value = 0

for sector in waste:
    value = waste[sector]

    if first:
        max_value = value
        min_value = value
        max_sector = sector
        min_sector = sector
        first = False
    else:
        if value > max_value:
            max_value = value
            max_sector = sector

        if value < min_value:
            min_value = value
            min_sector = sector

print("Maximum waste sector:", max_sector, max_value)
print("Minimum waste sector:", min_sector, min_value)

print("\n")

# -----------------------------
# 4. Total waste (NO sum)
# -----------------------------
total = 0

for sector in waste:
    total = total + waste[sector]

print("Total waste collected:", total)

print("\n")

# -----------------------------
# 5. Categorization
# -----------------------------
low = []
medium = []
high = []

for sector in waste:
    value = waste[sector]

    if value < 200:
        low.append(sector)

    elif value >= 200 and value <= 400:
        medium.append(sector)

    else:
        high.append(sector)

print("Low Waste (<200):", low)
print("Medium Waste (200–400):", medium)
print("High Waste (>400):", high)

print("\n")

# -----------------------------
# 6. Awareness campaign (>300)
# -----------------------------
campaign = []
count = 0

for sector in waste:
    if waste[sector] > 300:
        campaign.append(sector)
        count += 1

print("Sectors needing awareness campaigns (>300):", count)
print(campaign)

print("\n")

# -----------------------------
# 7. Save to file
# -----------------------------
file = open("campaign_sectors.txt", "w")

file.write("Awareness Campaign Sectors (>300 kg waste):\n")

for sector in campaign:
    file.write(sector + " - " + str(waste[sector]) + " kg\n")

file.close()

print("Data saved successfully in campaign_sectors.txt")