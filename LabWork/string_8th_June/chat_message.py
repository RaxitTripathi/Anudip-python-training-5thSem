""" 3. Chat Message Analytics 
Problem Statement 
A chat application stores a message: 
Python is awesome and Python is easy to learn 
Tasks 
Write a program to: 
1. Count total characters.  
2. Count total words.  
3. Find the longest word.  
4. Find the shortest word.  
5. Count how many times the word "Python" appears.  
6. Create a list of words having more than 4 characters.  
7. Display all words starting with a vowel.  
8. Count the number of vowels and consonants.   """

message = "Python is awesome and Python is easy to learn"

# Convert message into words
words = message.split()

# 1. Count total characters
total_characters = len(message)
print("Total Characters:", total_characters)

# 2. Count total words
total_words = len(words)
print("Total Words:", total_words)

# 3. Find the longest word
longest_word = words[0]

for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print("Longest Word:", longest_word)

# 4. Find the shortest word
shortest_word = words[0]

for word in words:
    if len(word) < len(shortest_word):
        shortest_word = word

print("Shortest Word:", shortest_word)

# 5. Count how many times "Python" appears
python_count = 0

for word in words:
    if word == "Python":
        python_count += 1

print("Python Appears:", python_count, "times")

# 6. Create list of words having more than 4 characters
more_than_4 = []

for word in words:
    if len(word) > 4:
        more_than_4.append(word)

print("Words with more than 4 characters:", more_than_4)

# 7. Display all words starting with a vowel
vowel_words = []

for word in words:
    if word[0].lower() in "aeiou":
        vowel_words.append(word)

print("Words starting with vowel:", vowel_words)

# 8. Count vowels and consonants
vowel_count = 0
consonant_count = 0

for ch in message:

    if ch.isalpha():

        if ch.lower() in "aeiou":
            vowel_count += 1
        else:
            consonant_count += 1

print("Total Vowels:", vowel_count)
print("Total Consonants:", consonant_count)


""" Output:

Total Characters: 45
Total Words: 9
Longest Word: awesome
Shortest Word: is
Python Appears: 2 times
Words with more than 4 characters: ['Python', 'awesome', 'Python', 'learn']
Words starting with vowel: ['is', 'awesome', 'and', 'is', 'easy']
Total Vowels: 14
Total Consonants: 23 """