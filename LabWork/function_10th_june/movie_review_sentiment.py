""" 3. Movie Review Sentiment Analyzer 
Problem Statement 
Movie reviews are stored as follows: 
reviews = [ 
    "excellent movie",  
    "average story", 
    "excellent acting", 
    "poor direction", 
    "excellent visuals", 
    "poor screenplay", 
    "good music", 
    "excellent climax", 
    "average performance", 
    "good cinematography" 
] 
Requirements 
Create the following functions: 
1. count_sentiments(reviews) 
Counts: 
• Excellent  
• Good  
• Average  
• Poor reviews  
2. most_common_word(reviews) 
Returns the most frequently occurring word. 
3. longest_review(reviews) 
Returns the review containing the maximum number of characters. 
4. reviews_with_keyword(reviews, keyword) 
Displays all reviews containing a given keyword.  """


# """ 1. count_sentiments(reviews) 
# Counts: 
# • Excellent  
# • Good  
# • Average  
# • Poor reviews  """
                

# 1. Count sentiments
def count_sentiments(reviews):
    excellent = 0
    good = 0
    average = 0
    poor = 0

    for review in reviews:
        if "excellent" in review:
            excellent += 1
        elif "good" in review:
            good += 1
        elif "average" in review:
            average += 1
        elif "poor" in review:
            poor += 1

    print("Excellent:", excellent)
    print("Good:", good)
    print("Average:", average)
    print("Poor:", poor)


# 2. Most common word
def most_common_word(reviews):
    freq = {}

    for review in reviews:
        words = review.split()

        for word in words:
            if word in freq:
                freq[word] += 1
            else:
                freq[word] = 1

    max_word = ""
    max_count = 0

    for word in freq:
        if freq[word] > max_count:
            max_count = freq[word]
            max_word = word

    return max_word


# 3. Longest review
def longest_review(reviews):
    longest = reviews[0]

    for review in reviews:
        if len(review) > len(longest):
            longest = review

    return longest


# 4. Reviews containing keyword
def reviews_with_keyword(reviews, keyword):
    print("Reviews containing", keyword, ":")

    review_find=0
    for review in reviews:
        if keyword in review.lower():
            print(review)
            review_find=1
    if review_find ==0:
        print("No review find related to Given keyword")            
        

#Main
reviews = [
    "excellent movie",
    "average story",
    "excellent acting",
    "poor direction",
    "excellent visuals",
    "poor screenplay",
    "good music",
    "excellent climax",
    "average performance",
    "good cinematography"
]

# Main Program
count_sentiments(reviews)

print("\nMost Common Word:", most_common_word(reviews))

print("Longest Review:", longest_review(reviews))

print()
user_keyword=input("Enter keyword:").lower()
reviews_with_keyword(reviews, user_keyword)


""" 
output:

Excellent: 4
Good: 2
Average: 2
Poor: 2

Most Common Word: excellent
Longest Review: average performance

Enter keyword:excellent
Reviews containing excellent :
excellent movie
excellent acting
excellent visuals
excellent climax """