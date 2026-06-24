def register_fir():

    fir_id = input("Enter FIR ID: ").strip()
    criminal_id = input("Enter Criminal ID: ").strip()
    crime_type = input("Enter Crime Type: ").strip()
    date = input("Enter Date: ").strip()

    try:
        with open("fir.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")

                if fir_id == data[0]:
                    print("FIR ID already exists!")
                    return

    except FileNotFoundError:
        pass

    with open("fir.txt", "a") as file:
        file.write(f"{fir_id},{criminal_id},{crime_type},{date}\n")

    print("FIR Registered Successfully!")


def view_firs():

    try:
        with open("fir.txt", "r") as file:

            print("\nFIR ID\tCriminal ID\tCrime\tDate")

            for line in file:
                data = line.strip().split(",")

                print(
                    f"{data[0]}\t{data[1]}\t{data[2]}\t{data[3]}"
                )

    except FileNotFoundError:
        print("No FIR records found!")


def search_fir():

    fir_id = input("Enter FIR ID: ").strip()

    try:
        with open("fir.txt", "r") as file:

            for line in file:
                data = line.strip().split(",")

                if fir_id == data[0]:

                    print("\nFIR Found")
                    print("FIR ID:", data[0])
                    print("Criminal ID:", data[1])
                    print("Crime Type:", data[2])
                    print("Date:", data[3])

                    return

            print("FIR not found!")

    except FileNotFoundError:
        print("No FIR records found!")


def update_fir():

    fir_id = input("Enter FIR ID: ").strip()

    try:
        with open("fir.txt", "r") as file:
            lines = file.readlines()

        updated = False

        for i in range(len(lines)):

            data = lines[i].strip().split(",")

            if fir_id == data[0]:

                criminal_id = input("Enter New Criminal ID: ")
                crime_type = input("Enter New Crime Type: ")
                date = input("Enter New Date: ")

                lines[i] = (
                    f"{fir_id},{criminal_id},"
                    f"{crime_type},{date}\n"
                )

                updated = True
                break

        if updated:

            with open("fir.txt", "w") as file:
                file.writelines(lines)

            print("FIR Updated Successfully!")

        else:
            print("FIR not found!")

    except FileNotFoundError:
        print("No FIR records found!")

def delete_fir():

    fir_id = input("Enter FIR ID: ").strip()

    try:
        with open("fir.txt", "r") as file:
            lines = file.readlines()

        new_lines = []
        deleted = False

        for line in lines:

            data = line.strip().split(",")

            if fir_id == data[0]:
                deleted = True
            else:
                new_lines.append(line)

        if deleted:

            with open("fir.txt", "w") as file:
                file.writelines(new_lines)

            print("FIR Deleted Successfully!")

        else:
            print("FIR not found!")

    except FileNotFoundError:
        print("No FIR records found!")        