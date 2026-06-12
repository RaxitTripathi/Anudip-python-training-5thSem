""" Problem 11: Student Feedback Analysis System 
Problem Statement 
A training institute collects feedback from students after completing a Python course. The feedback 
comments are stored in a text file named feedback.txt. 
Sample Input/Data (feedback.txt) 
The sessions were very interactive and informative. 
Excellent teaching methodology and practical examples. 
The pace of the course was appropriate. 
More real-world projects should be included. 
The trainer explained concepts very clearly. 
Tasks 
1. Count the total number of lines.  
2. Count the total number of words.  
3. Count the total number of characters.  
4. Find the longest feedback comment.  
5. Find the shortest feedback comment.  
6. Count the total number of vowels present in the file.  """


with open("feedback.txt","r") as file:
    # 1. Count the total number of lines.
    data=file.read()
    lines=data.split("\n")
    print("Total number of lines:",len(lines))
    # 2. Count the total number of words.  
    count_word=0
    for line in lines:
        word=line.split(" ")
        count_word += len(word)

    print("Total number of words:",count_word)    

    # 3. Count the total number of characters. 
    character=data.replace("\n","").replace(" ","")
    print("Total number of characters:",len(character))

    # 4. Find the longest feedback comment. 
    # 5. Find the shortest feedback comment.
    
    longest_feed="" 
    longest_size=0
    shortest_feed=""
    shortest_size=float("inf")

    for line in lines:
        if len(line) > longest_size:
            longest_size=len(line)
            longest_feed=line
        elif len(line) < shortest_size:
            shortest_size=len(line)
            shortest_feed=line

    print("\nLongest Feedback Comment:\n",longest_feed)
    print("\nShortest Feedback Comment:\n",shortest_feed)


    # 6. Count the total number of vowels present in the file. 

    count_vowels = 0

    for ch in data.lower():
        if ch in "aeiou":
            count_vowels += 1

    print("\nTotal vowels:", count_vowels)


""" output:

Total number of lines: 5
Total number of words: 36
Total number of characters: 205

Longest Feedback Comment:
 Excellent teaching methodology and practical examples. 

Shortest Feedback Comment:
 The pace of the course was appropriate. 

Total vowels: 75 """