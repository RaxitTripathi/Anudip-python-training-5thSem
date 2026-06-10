""" 5. City Population & Development Dashboard 

Problem Statement 
The government wants to analyze city data. 
Store details of at least 30 cities. 
Example Structure 
cities = { 
    "Delhi": { 
        "population": 32000000, 
        "area": 1484, 
        "literacy": 89 
    } 
} 
Requirements 
1. Display all city details.  
2. Find the most populated city.  
3. Find the least populated city.  
4. Calculate average population.  
5. Display cities with literacy rate above 90%.  
6. Display cities with literacy below average.  
7. Calculate population density.  
8. Find city with highest density.  
9. Categorize cities:  
o Small  
o Medium  
o Large  
10. Create a development-priority list.  
11. Generate separate dictionaries for:  
o High Literacy Cities  
o Low Literacy Cities  
12. Generate a national summary report.  
Challenge 
Rank all cities based on population density. """

from city_population_operations import *

cities = {}

# 1. Input 30 cities
print("Enter details of 30 cities:\n")

for i in range(30):
    print(f"\nCity {i+1}")

    name = input("Enter City Name: ")
    population = int(input("Enter Population: "))
    area = int(input("Enter Area: "))
    literacy = float(input("Enter Literacy Rate: "))

    cities[name] = {
        "population": population,
        "area": area,
        "literacy": literacy
    }

print("\nAll 30 cities added successfully!")


# 2. Menu
while True:

    print("\n----- CITY DASHBOARD -----")
    print("1. Display cities")
    print("2. Most populated city")
    print("3. Least populated city")
    print("4. Average population")
    print("5. Literacy > 90%")
    print("6. Literacy below average")
    print("7. Population density")
    print("8. Highest density city")
    print("9. Categorize cities")
    print("10. Development priority")
    print("11. Literacy groups")
    print("12. Summary report")
    print("13. Density ranking")
    print("14. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        display_cities(cities)

    elif choice == "2":
        most_populated(cities)

    elif choice == "3":
        least_populated(cities)

    elif choice == "4":
        average_population(cities)

    elif choice == "5":
        high_literacy(cities)

    elif choice == "6":
        low_literacy_average(cities)

    elif choice == "7":
        population_density(cities)

    elif choice == "8":
        highest_density(cities)

    elif choice == "9":
        categorize_cities(cities)

    elif choice == "10":
        development_priority(cities)

    elif choice == "11":
        literacy_groups(cities)

    elif choice == "12":
        summary_report(cities)

    elif choice == "13":
        density_ranking(cities)

    elif choice == "14":
        print("Exiting...")
        break

    else:
        print("Invalid choice")