# wap to input a sentence and display the frequency of vowel present ignore the case


user_input=input("Enter sentence:").lower()
vowel_dict={}

for letter in user_input:
    if letter in "aeiou":
        if letter in vowel_dict:
            vowel_dict[letter] +=1
        else:
            vowel_dict[letter]=1    


print("Total vowel in given sentence is:")
for vowel in vowel_dict:
    print(vowel,":",vowel_dict[vowel])            
        
     