def total_criminals():

    try:

        with open("criminals.txt", "r") as file:

            count = len(file.readlines())

            print("Total Criminals :", count)

    except FileNotFoundError:

        print("No Criminal Records Found!")


def total_firs():

    try:

        with open("fir.txt", "r") as file:

            count = len(file.readlines())

            print("Total FIRs :", count)

    except FileNotFoundError:

        print("No FIR Records Found!")


def total_cases():

    try:

        with open("cases.txt", "r") as file:

            count = len(file.readlines())

            print("Total Cases :", count)

    except FileNotFoundError:

        print("No Case Records Found!")


def open_cases():

    count = 0

    try:

        with open("cases.txt", "r") as file:

            for line in file:

                data = line.strip().split(",")

                if data[2] == "Open":

                    count += 1

        print("Open Cases :", count)

    except FileNotFoundError:

        print("No Case Records Found!")

def closed_cases():

    count = 0

    try:

        with open("cases.txt", "r") as file:

            for line in file:

                data = line.strip().split(",")

                if data[2] == "Closed":

                    count += 1

        print("Closed Cases :", count)

    except FileNotFoundError:

        print("No Case Records Found!")


def crime_statistics():

    crime_count = {}

    try:

        with open("criminals.txt", "r") as file:

            for line in file:

                data = line.strip().split(",")

                crime = data[3]

                if crime in crime_count:

                    crime_count[crime] += 1

                else:

                    crime_count[crime] = 1

        print("\nCrime Statistics")

        for crime, count in crime_count.items():

            print(f"{crime} : {count}")

    except FileNotFoundError:

        print("No Criminal Records Found!")                

