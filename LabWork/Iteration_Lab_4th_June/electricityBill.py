# Calculate electricity bill based on the following slab rates: 
# Units Rate 
# 0-100 ₹5/unit 
# 101-200 ₹7/unit 
# Above 200 ₹10/unit 
# Display: 
# • Units Consumed  
# • Total Bill  
# • Category (Low / Medium / High Consumption)  

units=int(input("Enter Electricity Unit: "))
if(units<0):
    exit("Units can't be in negative")
bill=0
if(units>0 or units<100):
    bill=units*5
    category="low"
elif(units>100  or units<201):
    bill=units*7
    category="Medium"
else:
    bill=units*10
    category="High consumption"

print("Units Consumed:",units)
print("Total bill:",bill)
print("Category:",category)    




