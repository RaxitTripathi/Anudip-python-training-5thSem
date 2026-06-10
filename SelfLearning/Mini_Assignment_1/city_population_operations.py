
# 1. Display all cities
def display_cities(cities):
    for city in cities:
        print(city, cities[city])


# 2. Most populated city
def most_populated(cities):

    max_city = None

    for city in cities:
        if max_city is None or cities[city]["population"] > cities[max_city]["population"]:
            max_city = city

    print("Most Populated:", max_city, cities[max_city]["population"])


# 3. Least populated city
def least_populated(cities):

    min_city = None

    for city in cities:
        if min_city is None or cities[city]["population"] < cities[min_city]["population"]:
            min_city = city

    print("Least Populated:", min_city, cities[min_city]["population"])


# 4. Average population
def average_population(cities):

    total = 0

    for city in cities:
        total += cities[city]["population"]

    avg = total / len(cities)

    print("Average Population =", int(avg))


# 5. Literacy > 90%
def high_literacy(cities):

    for city in cities:
        if cities[city]["literacy"] > 90:
            print(city, cities[city]["literacy"])


# 6. Literacy below average
def low_literacy_average(cities):

    total = 0

    for city in cities:
        total += cities[city]["literacy"]

    avg = total / len(cities)

    for city in cities:
        if cities[city]["literacy"] < avg:
            print(city, cities[city]["literacy"])


# 7. Population density
def population_density(cities):

    for city in cities:
        density = cities[city]["population"] / cities[city]["area"]
        print(city, int(density))


# 8. Highest density city
def highest_density(cities):

    max_city = None
    max_density = 0

    for city in cities:
        density = cities[city]["population"] / cities[city]["area"]

        if max_city is None or density > max_density:
            max_density = density
            max_city = city

    print("Highest Density:", max_city, int(max_density))


# 9. Categorize cities
def categorize_cities(cities):

    for city in cities:

        pop = cities[city]["population"]

        if pop < 5000000:
            print(city, "Small")

        elif pop < 20000000:
            print(city, "Medium")

        else:
            print(city, "Large")


# 10. Development priority (low literacy + high population)
def development_priority(cities):

    for city in cities:

        if cities[city]["literacy"] < 80 and cities[city]["population"] > 10000000:
            print(city, "High Priority")


# 11. High / Low literacy dictionaries
def literacy_groups(cities):

    high = {}
    low = {}

    for city in cities:

        if cities[city]["literacy"] >= 90:
            high[city] = cities[city]

        else:
            low[city] = cities[city]

    print("High Literacy Cities")
    for city in high:
        print(city, high[city])

    print("\nLow Literacy Cities")
    for city in low:
        print(city, low[city])


# 12. Summary report
def summary_report(cities):

    total_pop = 0
    total_lit = 0

    for city in cities:
        total_pop += cities[city]["population"]
        total_lit += cities[city]["literacy"]

    print("Total Cities =", len(cities))
    print("Total Population =", total_pop)
    print("Average Literacy =", total_lit / len(cities))


# 13. Rank cities by density (NO SORT FUNCTION)
def density_ranking(cities):

    temp = cities.copy()

    print("Density Ranking (Manual)")

    rank = 1

    while temp:

        max_city = None
        max_density = 0

        for city in temp:
            density = temp[city]["population"] / temp[city]["area"]

            if max_city is None or density > max_density:
                max_density = density
                max_city = city

        print(rank, max_city, int(max_density))

        temp.pop(max_city)
        rank += 1