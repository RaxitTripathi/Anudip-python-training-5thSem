""" Problem 5: Mobile Screen Time Analyzer 
Problem Statement 
Daily mobile screen time (in minutes) of a student is recorded for 10 days. 
Sample Data 
screen_time = [180, 220, 150, 300, 120, 250, 190, 210, 175, 260] 
Tasks 
1. Calculate average screen time.  
2. Find the highest and lowest screen time.  
3. Count days exceeding 200 minutes.  
4. Display days with healthy usage (<180 minutes).  
5. Categorize usage:  
o Healthy (<180)  
o Moderate (180–240)  
o Excessive (>240)  """

screen_time = [180, 220, 150, 300, 120, 250, 190, 210, 175, 260] 

avg_time=0
highest_time=0
lowest_time=float("inf")
days_200=0


for time in screen_time:
    if time > 200:
        days_200 +=1
    if time > highest_time:
        highest_time =time
    elif time < lowest_time:
        lowest_time =time
    avg_time +=time 

""" 1. Calculate average screen time.  
2. Find the highest and lowest screen time.  
3. Count days exceeding 200 minutes.   """

print("Avg screen Time:",avg_time/len(screen_time),"minutes")
print("\nHighest Time:",highest_time,"minutes")
print("Lowest Time:",lowest_time,"minutes")

# 4. Display days with healthy usage (<180 minutes).  
count_day=1
healthy=0
moderate=0
excessive=0
print("Healthy Usage Days:")
for time in screen_time:
    if time <180:
        print("Day:",count_day)
        healthy +=1
    elif time >=180 and time <240:
        moderate +=1

    else:
        excessive +=1        

           
    count_day +=1     

# 5. Categorize usage:  
# o Healthy (<180)  
# o Moderate (180–240)  
# o Excessive (>240)    


print("\nHealthy:",healthy)
print("MOderate:",moderate)
print("Excessive:",excessive)


""" output:

Avg screen Time: 205.5 minutes

Highest Time: 300 minutes
Lowest Time: 120 minutes
Healthy Usage Days:
Day: 3
Day: 5
Day: 9

Healthy: 3
MOderate: 4
Excessive: 3 """