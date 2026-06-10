""" Assignment 3: Chat Message Analytics Dashboard 
Problem Statement 
A messaging application wants to analyze chat messages. 
Store at least 20 chat messages in a list. 
Requirements 
For each message: 
1. Count total words.  
2. Count total characters.  
3. Count vowels and consonants.  
4. Find longest word.  
5. Find shortest word.  
6. Count occurrence of each word.  
7. Display repeated words.  
8. Display words starting with vowels.  
9. Display words longer than 5 characters.  
10. Create a dictionary containing word frequencies.  
Challenge 
Generate a report showing: 
Most Frequently Used Word 
Longest Message 
Shortest Message 
Average Words Per Message  """

# Chat Message Analytics Dashboard

messages = []

# Input 20 messages with proper validation
for i in range(20):
    while True:
        msg = input(f"Enter message {i+1}: ")
        if msg.strip() != "":
            break
        print("Invalid message, try again (empty not allowed)")

    messages.append(msg)

# Overall data
total_words_all = 0
word_freq = {}

longest_message = ""
shortest_message = messages[0]

print("\nMESSAGE ANALYSIS")
print("-" * 60)

for msg in messages:

    words = msg.split()
    word_count = len(words)
    char_count = len(msg)

    total_words_all += word_count

    vowels = 0
    consonants = 0

    longest_word = ""
    shortest_word = None

    print("\nMessage:", msg)
    print("Words:", word_count)
    print("Characters:", char_count)

    for word in words:

        clean_word = word.lower().strip(".,!?")

        # skip empty after cleaning
        if clean_word == "":
            continue

        # vowel & consonant count
        for ch in clean_word:
            if ch.isalpha():
                if ch in "aeiou":
                    vowels += 1
                else:
                    consonants += 1

        # longest word
        if len(clean_word) > len(longest_word):
            longest_word = clean_word

        # shortest word
        if shortest_word is None or len(clean_word) < len(shortest_word):
            shortest_word = clean_word

        # word frequency
        if clean_word in word_freq:
            word_freq[clean_word] += 1
        else:
            word_freq[clean_word] = 1

    print("Vowels:", vowels)
    print("Consonants:", consonants)
    print("Longest Word:", longest_word)
    print("Shortest Word:", shortest_word)

    # message-level tracking
    if len(msg) > len(longest_message):
        longest_message = msg

    if len(msg) < len(shortest_message):
        shortest_message = msg

print("\nWORD FREQUENCY REPORT")
print("-" * 60)

for word, count in word_freq.items():
    print(word, "->", count)

print("\nREPEATED WORDS")
print("-" * 60)

for word, count in word_freq.items():
    if count > 1:
        print(word, "->", count)

print("\nWORDS STARTING WITH VOWELS")
print("-" * 60)

for word in word_freq:
    if word and word[0] in "aeiou":
        print(word)

print("\nWORDS LONGER THAN 5 CHARACTERS")
print("-" * 60)

for word in word_freq:
    if len(word) > 5:
        print(word)

# FINAL REPORT
print("\nFINAL REPORT")
print("-" * 60)

most_freq_word = ""
max_count = 0

for word, count in word_freq.items():
    if count > max_count:
        max_count = count
        most_freq_word = word

avg_words = total_words_all / len(messages) if messages else 0

print("Most Frequently Used Word:", most_freq_word)
print("Longest Message:", longest_message)
print("Shortest Message:", shortest_message)
print("Average Words Per Message:", avg_words)