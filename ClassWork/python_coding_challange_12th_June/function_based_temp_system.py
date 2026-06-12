""" Problem 15: Function-Based Temperature Converter 
Problem Statement 
Daily temperatures recorded in Celsius are given below. 
Sample Data 
temperatures = [25, 30, 35, 40, 28, 32, 38, 22, 27, 31] 
Tasks 
Create functions to: 
1. Convert Celsius to Fahrenheit.  
2. Display all temperatures in Fahrenheit.  
3. Find the highest Fahrenheit temperature.  
4. Find the lowest Fahrenheit temperature.  
5. Calculate the average Fahrenheit temperature.  

°F = (°C x 1.8) + 32 

"""
temperatures = [25, 30, 35, 40, 28, 32, 38, 22, 27, 31]

# 1. Convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 1.8) + 32


# 2. Display all temperatures in Fahrenheit
def display_fahrenheit(temps):
    print("Temperatures in Fahrenheit:")
    for temp in temps:
        print(celsius_to_fahrenheit(temp))


# 3. Find highest Fahrenheit temperature
def highest_fahrenheit(temps):
    highest = celsius_to_fahrenheit(temps[0])

    for temp in temps:
        fahrenheit = celsius_to_fahrenheit(temp)

        if fahrenheit > highest:
            highest = fahrenheit

    return highest


# 4. Find lowest Fahrenheit temperature
def lowest_fahrenheit(temps):
    lowest = celsius_to_fahrenheit(temps[0])

    for temp in temps:
        fahrenheit = celsius_to_fahrenheit(temp)

        if fahrenheit < lowest:
            lowest = fahrenheit

    return lowest


# 5. Calculate average Fahrenheit temperature
def average_fahrenheit(temps):
    total = 0

    for temp in temps:
        total += celsius_to_fahrenheit(temp)

    return total / len(temps)


display_fahrenheit(temperatures)

print("\nHighest Temperature:", highest_fahrenheit(temperatures), "F")
print("Lowest Temperature:", lowest_fahrenheit(temperatures), "F")
print("Average Temperature:", average_fahrenheit(temperatures), "F")



""" output:

Temperatures Celsius to Fahrenheit:
77.0
86.0
95.0
104.0
82.4
89.6
100.4
71.6
80.6
87.80000000000001

Highest Temperature: 104.0 F

Lowest Temperature: 71.6 F

Average Temperature: 87.44000000000001 F """