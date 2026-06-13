""" Problem 5: Digital Library Plagiarism Detector 
Problem Statement 
Two research abstracts are provided as strings. 
abstract1 = "Artificial intelligence is transforming education and healthcare." 
abstract2 = "Healthcare and education are rapidly transforming through artificial intelligence." 
Tasks 
1. Convert both abstracts into sets of words.  
2. Identify common words.  
3. Identify unique words in each abstract.  
4. Calculate the percentage similarity.  
5. Display whether plagiarism review is required (similarity > 50%).  """


def plagiarism_check():

    abstract1 = "Artificial intelligence is transforming education and healthcare."
    abstract2 = "Healthcare and education are rapidly transforming through artificial intelligence."

    words1 = set(abstract1.lower().split())
    words2 = set(abstract2.lower().split())

    common = words1 & words2
    unique1 = words1 - words2
    unique2 = words2 - words1

    similarity = (len(common) / len(words1 | words2)) * 100

    print("Common Words:", common)
    print("Unique in Abstract1:", unique1)
    print("Unique in Abstract2:", unique2)
    print("Similarity =", similarity, "%")

    if similarity > 50:
        print("Plagiarism Review Required")
    else:
        print("No Review Required")


try:
    plagiarism_check() #checking how much two abstracts are similar.

except Exception as e:
    print("Error:", e)