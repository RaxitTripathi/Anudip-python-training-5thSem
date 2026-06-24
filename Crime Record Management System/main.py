from officer_authentication import *
from criminal_management import *
from fir_manage import *
from case_track import *
from search_filters import *
from report_statis import *
from evidence_manage import *
from most_wantedd import *
from witness_victim import *
from recovery_backup import *

def officer_authentication(is_login):
    while True:
        print("\n===== OFFICER AUTHENTICATION =====")
        print("1. Login")
        print("2. Create Officer Account")
        print("3. Change Password")
        print("4. Logout")
        print("5. Back")

        try:
            choice = int(input("Enter Choice: "))

            if choice == 1:
                is_login = login(is_login)

            elif choice == 2:
                create_officer_account(is_login)

            elif choice == 3:
                change_password(is_login)

            elif choice == 4:
                if is_login:
                    is_login = False
                    print("Logged Out Successfully!")
                else:
                    print("No user is currently logged in.")

            elif choice == 5:
                print("Returning to Main Menu...")
                return is_login

            else:
                print("Enter a number between 1 and 5.")

        except ValueError:
            print("Please enter a valid number.")


def criminal_management():

    while True:

        print("\n===== CRIMINAL RECORD MANAGEMENT =====")
        print("1. Add Criminal")
        print("2. View Criminals")
        print("3. Search Criminal")
        print("4. Update Criminal")
        print("5. Delete Criminal")
        print("6. Back")

        try:
            choice = int(input("Enter Choice: "))

            if choice == 1:
                add_criminal()

            elif choice == 2:
                view_criminals()

            elif choice == 3:
                search_criminal()

            elif choice == 4:
                update_criminal()

            elif choice == 5:
                delete_criminal()

            elif choice == 6:
                print("Returning to Main Menu...")
                break

            else:
                print("Enter a number between 1 and 6.")

        except ValueError:
            print("Please enter a valid number.")


def fir_management(is_login):

    
    while True:

        print("\n===== FIR MANAGEMENT =====")
        print("1. Register FIR")
        print("2. View FIRs")
        print("3. Search FIR")
        print("4. Update FIR")
        print("5. Delete FIR")
        print("6. Back")

        try:
            choice = int(input("Enter Choice: "))

            if choice == 1:
                register_fir()

            elif choice == 2:
                view_firs()

            elif choice == 3:
                search_fir()

            elif choice == 4:
                update_fir()

            elif choice == 5:
                delete_fir()

            elif choice == 6:
                break

            else:
                print("Enter a number between 1 and 6.")

        except ValueError:
            print("Invalid Input!")


def case_tracking():
    
    while True:

        print("\n===== CASE TRACKING =====")
        print("1. Open Case")
        print("2. View Cases")
        print("3. Search Case")
        print("4. Update Status")
        print("5. Delete Case")
        print("6. Back")

        try:
            choice = int(input("Enter Choice: "))

            if choice == 1:
                open_case()

            elif choice == 2:
                view_cases()

            elif choice == 3:
                search_case()

            elif choice == 4:
                update_case_status()

            elif choice == 5:
                delete_case()

            elif choice == 6:
                break

            else:
                print("Enter a number between 1 and 6.")

        except ValueError:
            print("Invalid Input!")


def search_filter():

    while True:

        print("\n===== SEARCH & FILTER =====")
        print("1. Search Criminal By ID")
        print("2. Search Criminal By Name")
        print("3. Search FIR By FIR ID")
        print("4. Search FIR By Criminal ID")
        print("5. Search Case By Case ID")
        print("6. Search Case By Status")
        print("7. Back")

        try:
            choice = int(input("Enter Choice: "))

            if choice == 1:
                search_criminal_id()

            elif choice == 2:
                search_criminal_name()

            elif choice == 3:
                search_fir_id()

            elif choice == 4:
                search_fir_criminal()

            elif choice == 5:
                search_case_id()

            elif choice == 6:
                search_case_status()

            elif choice == 7:
                break

            else:
                print("Enter number between 1 and 7.")

        except ValueError:
            print("Invalid Input!")


def reports_statistics():

    while True:

        print("\n===== REPORTS & STATISTICS =====")
        print("1. Total Criminals")
        print("2. Total FIRs")
        print("3. Total Cases")
        print("4. Open Cases")
        print("5. Closed Cases")
        print("6. Crime Wise Statistics")
        print("7. Back")

        try:

            choice = int(input("Enter Choice: "))

            if choice == 1:
                total_criminals()

            elif choice == 2:
                total_firs()

            elif choice == 3:
                total_cases()

            elif choice == 4:
                open_cases()

            elif choice == 5:
                closed_cases()

            elif choice == 6:
                crime_statistics()

            elif choice == 7:
                break

            else:
                print("Enter number between 1 and 7.")

        except ValueError:
            print("Invalid Input!")

def evidence_management():

    while True:

        print("\n===== EVIDENCE MANAGEMENT =====")
        print("1. Add Evidence")
        print("2. View Evidence")
        print("3. Search Evidence")
        print("4. Delete Evidence")
        print("5. Back")

        try:

            choice = int(input("Enter Choice: "))

            if choice == 1:
                add_evidence()

            elif choice == 2:
                view_evidence()

            elif choice == 3:
                search_evidence()

            elif choice == 4:
                delete_evidence()

            elif choice == 5:
                break

            else:
                print("Enter number between 1 and 5.")

        except ValueError:
            print("Invalid Input!")


def most_wanted():

    while True:

        print("\n===== MOST WANTED CRIMINALS =====")
        print("1. Add To Most Wanted")
        print("2. View Most Wanted List")
        print("3. Search Criminal")
        print("4. Remove Criminal")
        print("5. Back")

        try:

            choice = int(input("Enter Choice: "))

            if choice == 1:
                add_most_wanted()

            elif choice == 2:
                view_most_wanted()

            elif choice == 3:
                search_most_wanted()

            elif choice == 4:
                remove_most_wanted()

            elif choice == 5:
                break

            else:
                print("Enter number between 1 and 5.")

        except ValueError:
            print("Invalid Input!")


def victim_witness():

    while True:

        print("\n===== VICTIM & WITNESS MODULE =====")
        print("1. Add Victim")
        print("2. Add Witness")
        print("3. View Records")
        print("4. Search by FIR ID")
        print("5. Delete Record")
        print("6. Back")

        try:

            choice = int(input("Enter Choice: "))

            if choice == 1:
                add_victim()

            elif choice == 2:
                add_witness()

            elif choice == 3:
                view_victims_witness()

            elif choice == 4:
                search_vw()

            elif choice == 5:
                delete_vw()

            elif choice == 6:
                break

            else:
                print("Enter number between 1 and 6.")

        except ValueError:
            print("Invalid Input!")

def backup_recovery():

    while True:

        print("\n===== BACKUP & RECOVERY =====")
        print("1. Create Backup")
        print("2. Restore Backup")
        print("3. Back")

        try:

            choice = int(input("Enter Choice: "))

            if choice == 1:
                create_backup()

            elif choice == 2:
                restore_backup()

            elif choice == 3:
                break

            else:
                print("Enter number between 1 and 3.")

        except ValueError:
            print("Invalid Input!")


def dashboard():

    print("\n=================================")
    print("        POLICE DASHBOARD")
    print("=================================")

    try:

        # ---------------- Criminals ----------------
        with open("criminals.txt", "r") as file:
            criminals = len(file.readlines())
    except:
        criminals = 0

    try:

        # ---------------- FIRs ----------------
        with open("fir.txt", "r") as file:
            firs = len(file.readlines())
    except:
        firs = 0

    try:

        # ---------------- Cases ----------------
        with open("cases.txt", "r") as file:
            cases = file.readlines()

        total_cases = len(cases)
        open_cases = 0
        closed_cases = 0

        for line in cases:

            data = line.strip().split(",")

            if data[2] == "Open":
                open_cases += 1

            elif data[2] == "Closed":
                closed_cases += 1

    except:
        total_cases = 0
        open_cases = 0
        closed_cases = 0

    try:

        # -------- Crime Statistics --------
        crime_count = {}

        with open("criminals.txt", "r") as file:

            for line in file:

                data = line.strip().split(",")

                crime = data[3]

                if crime in crime_count:
                    crime_count[crime] += 1
                else:
                    crime_count[crime] = 1

        # Most common crime
        if crime_count:
            most_common_crime = max(crime_count, key=crime_count.get)
        else:
            most_common_crime = "N/A"

    except:
        most_common_crime = "N/A"

    # ---------------- DISPLAY ----------------
    print(f"Total Criminals : {criminals}")
    print(f"Total FIRs      : {firs}")
    print(f"Total Cases     : {total_cases}")
    print(f"Open Cases      : {open_cases}")
    print(f"Closed Cases    : {closed_cases}")
    print(f"Most Crime Type : {most_common_crime}")

    print("=================================\n")

is_login = False

while True:
    print("\n===== CRIME RECORD MANAGEMENT SYSTEM =====")
    print(f"Login Status: {'Logged In' if is_login else 'Not Logged In'}")

    print("1. Officer Authentication")
    print("2. Criminal Record Management")
    print("3. FIR Registration")
    print("4. Case Tracking")
    print("5. Search & Filter")
    print("6. Reports & Statistics")
    print("7. Evidence Management")
    print("8. Most Wanted Criminals")
    print("9. Victim & Witness Records")
    print("10. Backup & Recovery")
    print("11. Dashboard")
    print("12. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        is_login = officer_authentication(is_login)

    elif choice == "2":
        if is_login:
            criminal_management()
        else:
            print("Please login first!")

    elif choice == "3":
        if is_login:
            fir_management()
        else:
            print("Please login first!")

    elif choice == "4":
        if is_login:
            case_tracking()
        else:
            print("Please login first!")

    elif choice == "5":
        # Search & Filter Module
    # Used to quickly find Criminal, FIR,
    # and Case records using different filters
    # such as ID, Name, Criminal ID, and Status.
        if is_login:
            search_filter()
        else:
            print("Please login first!")

    elif choice == "6":
       #Helps officers analyze records and monitor investigation progress.
        if is_login:
            reports_statistics()
        else:
            print("Please login first!")

    elif choice == "7":
        # Helps officers store and track evidence collected during investigations.
        if is_login:
            evidence_management()
        else:
            print("Please login first!")

    elif choice == "8":
        if is_login:
            most_wanted()
        else:
            print("Please login first!")

    elif choice == "9":
        #This module stores details of victims and witnesses related to FIRs, helping in investigation and evidence collection by linking people involved in the case.
        if is_login:
            victim_witness()
        else:
            print("Please login first!")

    elif choice == "10":
        if is_login:
            backup_recovery()
        else:
            print("Please login first!")

    elif choice == "11":
        if is_login:
            dashboard()
        else:
            print("Please login first!")

    elif choice == "12":
        print("Exiting...")
        break

    else:
        print("Invalid Choice!")