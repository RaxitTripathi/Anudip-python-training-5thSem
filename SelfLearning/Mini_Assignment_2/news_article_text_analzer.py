""" Assignment 5: News Article Text Analyzer 
Problem Statement 
A news agency wants to analyze the content of an article. 
Use a paragraph containing at least 300 words. 
Requirements 
1. Count total characters.  
2. Count total words.  
3. Count total sentences.  
4. Count vowels and consonants.  
5. Find longest word.  
6. Find shortest word.  
7. Find the most frequent word.  
8. Create a dictionary of word frequencies.  
9. Display words appearing only once.  
10. Display words appearing more than 5 times.  
11. Count words starting with each alphabet.  
12. Display all unique words.  
Challenge 
Generate a complete text summary: 
Total Words 
Total Sentences 
Average Word Length 
Most Frequent Word 
Vocabulary Size """


# Step 1: Input paragraph

while True:
    text = input("Enter article paragraph (min 300 words): ").strip()
    if len(text.split()) >= 300:
        break
    print("Invalid input! Paragraph must contain at least 300 words.")

# Step 2: Initialization

words = text.split()
total_words = len(words)
total_chars = len(text)
sentences = 0

vowels = 0
consonants = 0

freq = {}
unique_words = set()

longest_word = ""
shortest_word = None

alpha_count = {}

# Step 3: Sentence count

for ch in text:
    if ch in ".!?":
        sentences += 1

# Step 4: Word processing

for word in words:

    clean = word.lower().strip(".,!?")

    if clean == "":
        continue

    if clean not in unique_words:
        unique_words.append(clean)

    if clean in freq:
        freq[clean] += 1
    else:
        freq[clean] = 1

    if shortest_word is None or len(clean) < len(shortest_word):
        shortest_word = clean

    if len(clean) > len(longest_word):
        longest_word = clean

    for ch in clean:
        if ch.isalpha():
            if ch in "aeiou":
                vowels += 1
            else:
                consonants += 1

    first = clean[0]
    if first.isalpha():
        if first in alpha_count:
            alpha_count[first] += 1
        else:
            alpha_count[first] = 1

# Step 5: Most frequent word

most_freq = ""
max_count = 0

for w in freq:
    if freq[w] > max_count:
        max_count = freq[w]
        most_freq = w

# Step 6: Words appearing once and more than 5 times

once_words = []
more_than_5 = []

for w in freq:
    if freq[w] == 1:
        once_words.append(w)
    if freq[w] > 5:
        more_than_5.append(w)

# Step 7: Average word length

total_len = 0

for w in words:
    clean = w.lower().strip(".,!?")
    total_len += len(clean)

if total_words != 0:
    avg_word_length = total_len / total_words
else:
    avg_word_length = 0

# Step 8: Output

print("\nRESULTS")
print("-" * 50)

print("Total Words:", total_words)
print("Total Sentences:", sentences)
print("Total Characters:", total_chars)
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Longest Word:", longest_word)
print("Shortest Word:", shortest_word)
print("Most Frequent Word:", most_freq)
print("Vocabulary Size:", len(unique_words))
print("Average Word Length:", avg_word_length)

print("\nWORDS APPEARING ONLY ONCE")
print("-" * 50)
for w in once_words:
    print(w)

print("\nWORDS APPEARING MORE THAN 5 TIMES")
print("-" * 50)
for w in more_than_5:
    print(w)

print("\nWORDS STARTING WITH ALPHABET COUNT")
print("-" * 50)
for k in sorted(alpha_count):
    print(k, "->", alpha_count[k])

print("\nUNIQUE WORDS")
print("-" * 50)

for w in unique_words:
    print(w)