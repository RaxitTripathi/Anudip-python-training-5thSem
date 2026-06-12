""" Problem 19: Word Frequency Analyzer 
Problem Statement 
A text file contains the following paragraph. 
Sample Input/Data (article.txt) 
Python is easy to learn. 
Python is powerful. 
Python supports multiple programming paradigms. 
Programming with Python is enjoyable. 
Tasks 
1. Count the total number of words.  
2. Count the frequency of each word.  
3. Find the most frequently occurring word.  
4. Display words appearing only once.  
5. Display all unique words.  """


def word_frequency_analyzer(filename):

    with open(filename, "r") as file:
        text = file.read().lower()

    words = text.replace(".", "").split()

    # Total words
    total_words = len(words)

    # Frequency count
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    # Most frequent word
    max_count = 0
    most_frequent = ""

    for word in frequency:
        if frequency[word] > max_count:
            max_count = frequency[word]
            most_frequent = word

    # Words appearing once
    print("Words Appearing Only Once:")
    for word in frequency:
        if frequency[word] == 1:
            print(word)

    # Unique words
    print("\nUnique Words:")
    for word in frequency:
        print(word)

    print("\nTotal Number of Words:", total_words)

    print("\nWord Frequencies:")
    for word in frequency:
        print(word, ":", frequency[word])

    print("\nMost Frequent Word:", most_frequent)
    print("Frequency:", max_count)


try:
    word_frequency_analyzer("article.txt")

except FileNotFoundError:
    print("Error: File not found.")

except Exception as e:
    print("Error:", e)