""" 3. City Temperature Monitoring System 
Problem Statement 
Daily temperatures of different cities are stored as: 
temperature = { 
    "Delhi": 41, 
    "Mumbai": 33, 
    "Chennai": 37, 
    "Kolkata": 39, 
    "Bengaluru": 28, 
    "Pune": 30, 
    "Jaipur": 42, 
    "Lucknow": 40, 
    "Hyderabad": 35, 
    "Ahmedabad": 43 
} 
Tasks 
1. Display cities having temperature above 40°C.  
2. Find the hottest city.  
3. Find the coolest city.  
4. Calculate average temperature.  
5. Create a list of pleasant cities (temperature < 35°C).  
6. Count cities with temperature between 35°C and 40°C.  """

temperature = {
    "Delhi": 41,
    "Mumbai": 33,
    "Chennai": 37,
    "Kolkata": 39,
    "Bengaluru": 28,
    "Pune": 30,
    "Jaipur": 42,
    "Lucknow": 40,
    "Hyderabad": 35,
    "Ahmedabad": 43
}

# 1. Cities having temperature above 40°C
print("Cities Above 40°C:")
for city, temp in temperature.items():
    if temp > 40:
        print(city, ":", temp)

# 2. Find the hottest city
hottest_city = None
highest_temp = 0

for city, temp in temperature.items():
    if temp > highest_temp:
        highest_temp = temp
        hottest_city = city

print("\nHottest City:")
print(hottest_city, ":", highest_temp)

# 3. Find the coolest city
coolest_city = None
lowest_temp = float('inf')

for city, temp in temperature.items():
    if temp < lowest_temp:
        lowest_temp = temp
        coolest_city = city

print("\nCoolest City:")
print(coolest_city, ":", lowest_temp)

# 4. Calculate average temperature
total = 0

for temp in temperature.values():
    total += temp

average = total / len(temperature)

print("\nAverage Temperature:", average)

# 5. Pleasant cities (temperature < 35°C)
pleasant_cities = []

for city, temp in temperature.items():
    if temp < 35:
        pleasant_cities.append(city)

print("\nPleasant Cities:", pleasant_cities)

# 6. Count cities with temperature between 35°C and 40°C
count = 0

for temp in temperature.values():
    if 35 <= temp <= 40:
        count += 1

print("\nCities with Temperature Between 35°C and 40°C:", count)

""" output:

Cities Above 40°C:
Delhi : 41
Jaipur : 42
Ahmedabad : 43

Hottest City:
Ahmedabad : 43

Coolest City:
Bengaluru : 28

Average Temperature: 36.8

Pleasant Cities: ['Mumbai', 'Bengaluru', 'Pune']

Cities with Temperature Between 35°C and 40°C: 4 """ 