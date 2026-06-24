def add_most_wanted():

    criminal_id = input("Enter Criminal ID: ")
    name = input("Enter Criminal Name: ")
    reward = input("Enter Reward Amount: ")

    try:

        with open("wanted.txt", "r") as file:

            for line in file:

                data = line.strip().split(",")

                # Prevent duplicate IDs
                if criminal_id == data[0]:

                    print("Criminal already in Most Wanted List!")
                    return

    except FileNotFoundError:
        pass

    with open("wanted.txt", "a") as file:

        file.write(
            f"{criminal_id},{name},{reward}\n"
        )

    print("Added To Most Wanted List Successfully!")


def view_most_wanted():

    try:

        with open("wanted.txt", "r") as file:

            print("\nCriminal ID\tName\tReward")
            print("-" * 40)

            for line in file:

                data = line.strip().split(",")

                print(
                    f"{data[0]}\t{data[1]}\t₹{data[2]}"
                )

    except FileNotFoundError:

        print("No Most Wanted Records Found!")


def search_most_wanted():

    criminal_id = input("Enter Criminal ID: ")

    try:

        with open("wanted.txt", "r") as file:

            for line in file:

                data = line.strip().split(",")

                if criminal_id == data[0]:

                    print("\nCriminal Found")
                    print("Criminal ID :", data[0])
                    print("Name :", data[1])
                    print("Reward : ₹", data[2])

                    return

            print("Criminal not found!")

    except FileNotFoundError:

        print("No Most Wanted Records Found!")



def remove_most_wanted():

    criminal_id = input("Enter Criminal ID: ")

    try:

        with open("wanted.txt", "r") as file:

            lines = file.readlines()

        new_lines = []
        removed = False

        for line in lines:

            data = line.strip().split(",")

            if criminal_id == data[0]:

                # Skip record
                removed = True

            else:

                new_lines.append(line)

        if removed:

            with open("wanted.txt", "w") as file:

                file.writelines(new_lines)

            print("Removed Successfully!")

        else:

            print("Criminal not found!")

    except FileNotFoundError:

        print("No Most Wanted Records Found!")                    