# 2. Write a program to copy entire content from one file into another

#Open file in read operation
file = open('sentences.txt', 'r')

# Read all content
content = file.read()


file.close()

#Open file in write operation
copy_file = open('copy.txt', 'w')

# Write content into destination file
copy_file.write(content)


copy_file.close()

print("Content copied successfully.")

