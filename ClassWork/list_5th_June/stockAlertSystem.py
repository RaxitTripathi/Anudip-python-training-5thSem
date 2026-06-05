'''Problem Statement 
An inventory manager stores stock quantities as: 
stock = [25, 5, 0, 12, 3, 18, 0, 30] 
Write a program to: 
1. Display products that are out of stock.  
2. Display products that need restocking (quantity less than 10).  
3. Count available products.  
4. Create a new list containing only products with stock greater than or equal to 15.'''

#Given list
stock = [25, 5, 0, 12, 3, 18, 0, 30] 


out_stock_count=0
available_count=0
restock_product=[]
new_stock=[]


for i in stock:

    #count out of staock and available products
    if i == 0:
        out_stock_count +=1

    else:
        available_count +=1

    #Restock Required
    if(i<10):
        restock_product.append(i)

    #Healthy Stock
    if(i>15):
        new_stock.append(i)    

print("Out of Stock Products: ",out_stock_count)        
print("Restock Required: ",restock_product)  
print("Available Products: ",available_count)  
print("Healthy Stock:",new_stock)  