def add_evidence():

    case_id = input("Enter Case ID: ")
    evidence_id = input("Enter Evidence ID: ")
    description = input("Enter Evidence Description: ")

    try:

        with open("evidence.txt", "r") as file:

            for line in file:

                data = line.strip().split(",")

                # Prevent duplicate Evidence IDs
                if evidence_id == data[1]:

                    print("Evidence ID already exists!")
                    return

    except FileNotFoundError:
        pass

    with open("evidence.txt", "a") as file:

        file.write(
            f"{case_id},{evidence_id},{description}\n"
        )

    print("Evidence Added Successfully!")


def view_evidence():

    try:

        with open("evidence.txt", "r") as file:

            print("\nCase ID\tEvidence ID\tDescription")
            print("-" * 50)

            for line in file:

                data = line.strip().split(",")

                print(
                    f"{data[0]}\t{data[1]}\t{data[2]}"
                )

    except FileNotFoundError:

        print("No Evidence Records Found!")

def search_evidence():

    evidence_id = input("Enter Evidence ID: ")

    try:

        with open("evidence.txt", "r") as file:

            for line in file:

                data = line.strip().split(",")

                if evidence_id == data[1]:

                    print("\nEvidence Found")
                    print("Case ID :", data[0])
                    print("Evidence ID :", data[1])
                    print("Description :", data[2])

                    return

            print("Evidence not found!")

    except FileNotFoundError:

        print("No Evidence Records Found!")


def delete_evidence():

    evidence_id = input("Enter Evidence ID: ")

    try:

        with open("evidence.txt", "r") as file:

            lines = file.readlines()

        new_lines = []
        deleted = False

        for line in lines:

            data = line.strip().split(",")

            if evidence_id == data[1]:

                # Skip evidence record
                deleted = True

            else:

                new_lines.append(line)

        if deleted:

            with open("evidence.txt", "w") as file:

                file.writelines(new_lines)

            print("Evidence Deleted Successfully!")

        else:

            print("Evidence not found!")

    except FileNotFoundError:

        print("No Evidence Records Found!")

                                