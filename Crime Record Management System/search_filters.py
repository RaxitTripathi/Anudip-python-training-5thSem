def search_criminal_id():

    cid = input("Enter Criminal ID: ")

    try:

        with open("criminals.txt", "r") as file:

            for line in file:

                data = line.strip().split(",")

                if cid == data[0]:

                    print("\nRecord Found")
                    print("ID:", data[0])
                    print("Name:", data[1])
                    print("Age:", data[2])
                    print("Crime:", data[3])

                    return

            print("Criminal not found!")

    except FileNotFoundError:
        print("criminals.txt not found!")


def search_criminal_name():

    name = input("Enter Name: ").lower()

    found = False

    try:

        with open("criminals.txt", "r") as file:

            for line in file:

                data = line.strip().split(",")

                if name in data[1].lower():

                    print(
                        f"{data[0]} | {data[1]} | {data[2]} | {data[3]}"
                    )

                    found = True

            if not found:
                print("No matching records found!")

    except FileNotFoundError:
        print("criminals.txt not found!")



def search_fir_id():

    fir_id = input("Enter FIR ID: ")

    try:

        with open("fir.txt", "r") as file:

            for line in file:

                data = line.strip().split(",")

                if fir_id == data[0]:

                    print("\nFIR Found")
                    print("FIR ID :", data[0])
                    print("Criminal ID :", data[1])
                    print("Crime :", data[2])
                    print("Date :", data[3])

                    return

            print("FIR not found!")

    except FileNotFoundError:
        print("fir.txt not found!")



def search_fir_criminal():

    cid = input("Enter Criminal ID: ")

    found = False

    try:

        with open("fir.txt", "r") as file:

            for line in file:

                data = line.strip().split(",")

                if cid == data[1]:

                    print(
                        f"{data[0]} | {data[1]} | {data[2]} | {data[3]}"
                    )

                    found = True

            if not found:
                print("No FIR found!")

    except FileNotFoundError:
        print("fir.txt not found!")


def search_case_id():

    case_id = input("Enter Case ID: ")

    try:

        with open("cases.txt", "r") as file:

            for line in file:

                data = line.strip().split(",")

                if case_id == data[0]:

                    print("\nCase Found")
                    print("Case ID :", data[0])
                    print("FIR ID :", data[1])
                    print("Status :", data[2])

                    return

            print("Case not found!")

    except FileNotFoundError:
        print("cases.txt not found!")



def search_case_status():

    status = input("Enter Status: ").lower()

    found = False

    try:

        with open("cases.txt", "r") as file:

            for line in file:

                data = line.strip().split(",")

                if status == data[2].lower():

                    print(
                        f"{data[0]} | {data[1]} | {data[2]}"
                    )

                    found = True

            if not found:
                print("No case found!")

    except FileNotFoundError:
        print("cases.txt not found!")                                        