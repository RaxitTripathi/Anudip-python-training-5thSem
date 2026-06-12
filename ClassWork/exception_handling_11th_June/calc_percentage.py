""" #Calculate the total marks and percentage.
Determine the performance category:
20% to 50% → Average Student
Above 50% to 90% → Good Student
Above 90% → Excellent Student
Below 20% → Poor Student
Display the effect of individual subjects on the total:
Calculate and display the percentage contribution of Hindi marks to the total.
Calculate and display the percentage contribution of English marks to the total. """

try:
    # Input marks
    hindi = float(input("Enter Hindi marks: "))
    if hindi < 0 or hindi >100:
        raise Exception("Marks between 0-100")
    english = float(input("Enter English marks: "))
    if english < 0 or english >100:
        raise Exception("Marks between 0-100")
    math = float(input("Enter Math marks: "))
    if math < 0 or math >100:
        raise Exception("Marks between 0-100")
    science = float(input("Enter Science marks: "))
    if science < 0 or science >100:
        raise Exception("Marks between 0-100")

    # Total marks
    total_marks = hindi + english + math + science

    # Percentage (assuming each subject is out of 100)
    percentage = (total_marks / 400) * 100

    print("\n--- RESULT ---")
    print("Total Marks:", total_marks)
    print("Percentage:", percentage)

    # Performance category
    if percentage < 20:
        print("Category: Poor Student")
    elif percentage <= 50:
        print("Category: Average Student")
    elif percentage <= 90:
        print("Category: Good Student")
    else:
        print("Category: Excellent Student")

    # Contribution of subjects
    hindi_contribution = (hindi / total_marks) * 100
    english_contribution = (english / total_marks) * 100

    print("\n--- SUBJECT CONTRIBUTION ---")
    print("Hindi contribution:", hindi_contribution, "%")
    print("English contribution:", english_contribution, "%")

except ValueError:
    print("Error: Please enter numeric values only.")
except ZeroDivisionError:
    print("Error: Total marks is zero, cannot calculate percentage.")