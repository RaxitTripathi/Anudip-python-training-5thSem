""" Assignment 6: Student Resume Analyzer 
Problem Statement 
A student enters a resume as plain text (Name, Skills, Education, Projects, Achievements). 
The system should: 
1. Count total words.  
2. Count total characters.  
3. Extract email IDs.  
4. Extract phone numbers.  
5. Count skills mentioned.  
6. Find repeated keywords.  
7. Identify the most frequently used word.  
8. Generate a skill frequency report.  
9. Detect duplicate skills.  
10. Create a summary dashboard.  """


# Step 1: Input resume text
resume = input("Enter resume text: ").strip()

# Step 2: Basic counts
words = resume.split()
total_words = len(words)
total_chars = len(resume)

# Step 3: Extract email and phone
emails = []
phones = []

for w in words:
    if "@" in w and "." in w:
        emails.append(w)

    if w.isdigit() and len(w) == 10:
        phones.append(w)

# Step 4: Word frequency
freq = {}

for w in words:
    clean = w.lower().strip(".,!?")
    if clean in freq:
        freq[clean] += 1
    else:
        freq[clean] = 1

# Step 5: Most frequent word
most_freq = ""
max_count = 0

for w in freq:
    if freq[w] > max_count:
        max_count = freq[w]
        most_freq = w

# Step 6: Skills (simple assumption: words after "skills")
skills = []
skill_flag = False

for w in words:
    if w.lower() == "skills":
        skill_flag = True
        continue

    if skill_flag:
        skills.append(w.lower().strip(".,!?"))

# Step 7: Skill frequency
skill_freq = {}

for s in skills:
    if s in skill_freq:
        skill_freq[s] += 1
    else:
        skill_freq[s] = 1

# Step 8: Duplicate skills
duplicate_skills = []

for s in skill_freq:
    if skill_freq[s] > 1:
        duplicate_skills.append(s)

# Step 9: Repeated keywords
repeated = []

for w in freq:
    if freq[w] > 1:
        repeated.append(w)

# Step 10: Output dashboard
print("\nRESUME ANALYSIS DASHBOARD")
print("-" * 50)

print("Total Words:", total_words)
print("Total Characters:", total_chars)

print("\nEmails:")
for e in emails:
    print(e)

print("\nPhone Numbers:")
for p in phones:
    print(p)

print("\nMost Frequent Word:", most_freq)

print("\nRepeated Keywords:")
for r in repeated:
    print(r)

print("\nSkill Frequency Report:")
for s in skill_freq:
    print(s, "->", skill_freq[s])

print("\nDuplicate Skills:")
for d in duplicate_skills:
    print(d)