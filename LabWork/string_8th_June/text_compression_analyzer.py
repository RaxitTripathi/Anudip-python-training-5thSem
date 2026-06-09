""" 10. Text Compression Analyzer 
Problem Statement 
A compressed message is given: 
AAABBBCCCDDDAAA 
Tasks 
Write a program to: 
1. Count occurrences of each character.  
2. Create a dictionary of character frequencies.  
3. Display unique characters.  
4. Find the most frequent character.  
5. Create a compressed output:  
A3B3C3D3A3 
6. Calculate compression ratio.  """

message="AAABBBCCCDDDAAA"

# 1. Count occurrences of each character.  
msg_dict={}
for char in message:
    if char in msg_dict:
        msg_dict[char] +=1
    else:
        msg_dict[char] =1
print("\nOccurance of each character:")
for char in msg_dict:
    print(char,":",msg_dict[char])

#   2. Create a dictionary of character frequencies.              
print("\nDictionary of character frequencies:")
print(msg_dict)

# 3. Display unique characters.
print("\nUnique Characters:")
unique_list=[]
for char in msg_dict:
    unique_list.append(char)

print(unique_list)

# 4. Find the most frequent character.
most_freq_no=0
most_freq_char=None

for char in msg_dict:
    if msg_dict[char] > most_freq_no:
        most_freq_no=msg_dict[char]
        most_freq_char=char

print("Most Frequent Character:",most_freq_char)

""" 
5. Create a compressed output:  
A3B3C3D3A3 """

compressed = ""
count = 1

for i in range(1, len(message)):
    if message[i] == message[i-1]:
        count += 1
    else:
        compressed += message[i-1] + str(count)
        count = 1

# last group
compressed += message[-1] + str(count)

print("Compressed Output:", compressed)


""" output:


Occurance of each character:
A : 6
B : 3
C : 3
D : 3

Dictionary of character frequencies:
{'A': 6, 'B': 3, 'C': 3, 'D': 3}

Unique Characters:
['A', 'B', 'C', 'D']
Most Frequent Character: A
Compressed Output: A3B3C3D3A3 """