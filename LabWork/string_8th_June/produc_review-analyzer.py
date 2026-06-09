""" 5. Product Review Analyzer 
Problem Statement 
A customer submits a review: 
This product is excellent excellent excellent and very useful 
Tasks 
Write a program to: 
1. Count total words.  
2. Create a dictionary containing word frequencies.  
3. Find the most frequently used word.  
4. Find all words appearing only once.  
5. Count words having more than 5 characters.  
6. Display words in reverse order.  
7. Create a list of unique words.   """

review = "This product is excellent excellent excellent and very useful"

# Convert sentence into list of words
words = review.split()

# 1. Count total words
total_words = len(words)
print("Total Words:", total_words)

# 2. Create dictionary of word frequencies
freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print("Word Frequencies:", freq)

# 3. Find most frequently used word
max_word = words[0]
max_count = freq[max_word]

for word in freq:
    if freq[word] > max_count:
        max_word = word
        max_count = freq[word]

print("Most Frequent Word:", max_word)

# 4. Find words appearing only once
once_words = []

for word in freq:
    if freq[word] == 1:
        once_words.append(word)

if len(once_words) == 0:
    print("Words appearing once: No such words found")
else:
    print("Words appearing once:", once_words)

# 5. Count words having more than 5 characters
count_long_words = 0

for word in words:
    if len(word) > 5:
        count_long_words += 1

print("Words with more than 5 characters:", count_long_words)

# 6. Display words in reverse order
print("Words in reverse order:")

for i in range(len(words) - 1, -1, -1):
    print(words[i], end=" ")

print()

# 7. Create list of unique words
unique_words = []

for word in freq:
    unique_words.append(word)

if len(unique_words) == 0:
    print("Unique Words: No unique words found")
else:
    print("Unique Words:", unique_words)
    
""" output:

Total Words: 9
Word Frequencies: {'This': 1, 'product': 1, 'is': 1, 'excellent': 3, 'and': 1, 'very': 1, 'useful': 1}
Most Frequent Word: excellent
Words appearing once: ['This', 'product', 'is', 'and', 'very', 'useful']
Words with more than 5 characters: 5
Words in reverse order:
useful very and excellent excellent excellent is product This 
Unique Words: ['This', 'product', 'is', 'excellent', 'and', 'very', 'useful'] """