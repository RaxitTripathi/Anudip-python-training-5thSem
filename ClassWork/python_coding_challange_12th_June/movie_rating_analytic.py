""" 
Problem 10: Movie Rating Analysis System 
Problem Statement 
Ratings given by users for movies are stored below. 
Sample Data 
ratings = { 
    "Inception": 4.8, 
    "Avatar": 4.3, 
    "Titanic": 4.5, 
    "Joker": 4.7, 
    "Frozen": 3.8, 
    "Interstellar": 4.9, 
    "Dune": 4.6, 
    "Up": 4.1, 
    "Coco": 4.4, 
    "Cars": 3.9 
} 
Tasks 
1. Display movies rated above 4.5.  
2. Find the highest-rated movie.  
3. Find the lowest-rated movie.  
4. Calculate average rating.  
5. Create a recommendation list (rating ≥ 4.5).  """

ratings = { 
    "Inception": 4.8, 
    "Avatar": 4.3, 
    "Titanic": 4.5, 
    "Joker": 4.7, 
    "Frozen": 3.8, 
    "Interstellar": 4.9, 
    "Dune": 4.6, 
    "Up": 4.1, 
    "Coco": 4.4, 
    "Cars": 3.9 
} 

high_rated =0
high_rated_movie=""
low_rated =float("inf")
low_rated_movie=""
avg_rate =0
recommedation_list=[]


print("Movies rated above 4.5:")
for movie,rate in ratings.items():
    if rate > 4.5:
        print(movie)    
    if rate >= 4.5:
        recommedation_list.append(movie)    
    if  rate > high_rated:
        high_rated_movie =movie
        high_rated =rate
    elif rate < low_rated:
        low_rated_movie =movie
    avg_rate +=rate


#    2. Find the highest-rated movie.  

print("\nHighest Rated Movie:\n",high_rated_movie)

# 3. Find the lowest-rated movie.

print("\nLowest Rated Movie:\n",low_rated_movie)

# 4. Calculate average rating. 
print("\nAverage Rating:",avg_rate/len(ratings))

# 5. Create a recommendation list (rating ≥ 4.5). 
print("\nRecommended Movies:\n",recommedation_list)


""" output:

Movies rated above 4.5:
Inception
Joker
Interstellar
Dune

Highest Rated Movie:
 Interstellar

Lowest Rated Movie:
 Cars

Average Rating: 4.4

Recommended Movies:
 ['Inception', 'Titanic', 'Joker', 'Interstellar', 'Dune'] """