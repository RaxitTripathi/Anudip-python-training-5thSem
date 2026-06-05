'''Problem Statement 
Given a list: 
numbers = [4, 5, 6, 10, 11, 15, 16, 17] 
Write a program to find all pairs of consecutive numbers. 

Store all consecutive pairs in a new list. 
[(4,5), (5,6), (10,11), (15,16), (16,17)] '''

#Given list
numbers = [4, 5, 6, 10, 11, 15, 16, 17] 
consecutive_pairs=[]

#Cheaking consicutive or not
for i in range(len(numbers)-1):
    if(numbers[i]+1 == numbers[i+1]):
        print(numbers[i],"and",numbers[i+1],"are consecutive")
        consecutive_pairs.append((numbers[i], numbers[i + 1]))

print("Consecutive pairs:")
print(consecutive_pairs)        