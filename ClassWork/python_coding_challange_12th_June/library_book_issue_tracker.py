""" Problem 13: Library Book Issue Tracker 
Problem Statement 
A library stores the number of times books were issued during a month. 
Sample Data 
book_issues = [15, 8, 22, 10, 18, 5, 30, 12, 20, 25] 
Tasks 
1. Find the maximum number of issues.  
2. Find the minimum number of issues.  
3. Calculate the average number of issues.  
4. Count books issued more than 15 times.  
5. Create a list of books issued fewer than 10 times.  """


book_issues = [15, 8, 22, 10, 18, 5, 30, 12, 20, 25] 



max_issue=0
count_max_issue=0
min_issue=float("inf")
count_min_issue=0
avg_issue =0
book_issue_more_15 =0
book_issue_fewer_10 =[]
for book in book_issues:
    # 4. Count books issued more than 15 times.
    if book >15:
        book_issue_more_15 +=1
    #5. Create a list of books issued fewer than 10 times. 
    if book <10:
        book_issue_fewer_10.append(book) 

    #1. Find the maximum number of issues.
    if book >max_issue:
        count_max_issue +=1
        max_issue =book
    #2. Find the minimum number of issues.      
    elif book <min_issue:
        count_min_issue +=1
        min_issue =book
    #3. Calculate the average number of issues.  
    avg_issue += book      


print("Maximum Issues:",max_issue)
print("\nMinimum Issues:",min_issue)
print("\nAverage Issues:",avg_issue/len(book_issues))
print("\nBooks Issued More Than 15 Times:",book_issue_more_15)
print("\nBooks Issued Fewer Than 10 Times:\n",book_issue_fewer_10)

""" 
output:

Maximum Issues: 30

Minimum Issues: 5

Average Issues: 16.5

Books Issued More Than 15 Times: 5

Books Issued Fewer Than 10 Times:
 [8, 5] """