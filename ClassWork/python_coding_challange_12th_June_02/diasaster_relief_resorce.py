"""Problem 4: Disaster Relief Resource Allocation 
Problem Statement 
Relief materials available at different warehouses are stored as dictionaries. 
 resources = { 
    "Warehouse1":["Food", "Medicine", "Blankets"],  
    "Warehouse2": ["Water", "Food", "Tents"], 
    "Warehouse3": ["Medicine", "Tents", "Clothes"], 
    "Warehouse4": ["Food", "Water", "Medicine"] 
} 

Tasks 
1. Display all unique relief items.  
2. Find warehouses containing medicines.  
3. Count how many warehouses stock each resource.  
4. Identify the most widely available resource.  
5. Display resources available in all warehouses.  """


def disaster_relief(resources):

    unique_resources = set()
    resource_count = {}

    print("Warehouses Containing Medicine:")

    for warehouse, items in resources.items():

        # Unique resources
        for item in items:
            unique_resources.add(item)

            if item in resource_count:
                resource_count[item] += 1
            else:
                resource_count[item] = 1

        # Warehouses with Medicine
        if "Medicine" in items:
            print(warehouse)

    print("\nAll Unique Relief Items:")
    print(unique_resources)

    print("\nResource Availability Count:")
    for resource, count in resource_count.items():
        print(resource, ":", count)

    # Most widely available resource
    max_count = 0
    most_available = ""

    for resource, count in resource_count.items():
        if count > max_count:
            max_count = count
            most_available = resource

    print("\nMost Widely Available Resource:")
    print(most_available, "-", max_count, "warehouses")

    # Resources available in all warehouses
    common_resources = set(resources["Warehouse1"])

    for warehouse, items in resources.items():
        common_resources = common_resources.intersection(set(items))

    print("\nResources Available In All Warehouses:")
    print(common_resources)


try:
    resources = {
        "Warehouse1": ["Food", "Medicine", "Blankets"],
        "Warehouse2": ["Water", "Food", "Tents"],
        "Warehouse3": ["Medicine", "Tents", "Clothes"],
        "Warehouse4": ["Food", "Water", "Medicine"]
    }

    if len(resources) == 0:
        raise ValueError("No warehouse data available.")

    disaster_relief(resources)

except ValueError as e:
    print("Error:", e)

except Exception as e:
    print("Unexpected Error:", e) 