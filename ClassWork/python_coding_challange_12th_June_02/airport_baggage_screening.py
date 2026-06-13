""" Problem 2: Airport Baggage Screening System 
Problem Statement 
Passenger baggage weights (in kg) are stored as tuples: 
baggage = ( 
("P101", 18), 
("P102", 32), 
("P103", 24), 
("P104", 36), 
("P105", 28), 
("P106", 20), 
("P107", 41), 
("P108", 26), 
("P109", 19), 
("P110", 34) 
) 
Tasks 
1. Display passengers carrying baggage above 30 kg.  
2. Count passengers within and exceeding limits.  
3. Calculate excess baggage charges (₹500 per kg above 30 kg).  
4. Create a list of passengers requiring manual inspection.  
5. Find the passenger carrying the heaviest baggage.  """

def baggage_screening(baggage):

    within_limit = 0
    exceeding_limit = 0

    manual_inspection = []

    heaviest_passenger = ""
    max_weight = 0

    print("Passengers Carrying Baggage Above 30 kg:")

    for passenger, weight in baggage:

        if weight > 30:
            print(passenger, ":", weight, "kg")
            exceeding_limit += 1

            excess_charge = (weight - 30) * 500
            print("Excess Charge: ₹", excess_charge)

            manual_inspection.append(passenger)

        else:
            within_limit += 1

        if weight > max_weight:
            max_weight = weight
            heaviest_passenger = passenger

    print("\nPassengers Within Limit:", within_limit)
    print("Passengers Exceeding Limit:", exceeding_limit)

    print("\nPassengers Requiring Manual Inspection:")
    print(manual_inspection)

    print("\nHeaviest Baggage:")
    print(heaviest_passenger, "-", max_weight, "kg")


try:
    baggage = (
        ("P101", 18),
        ("P102", 32),
        ("P103", 24),
        ("P104", 36),
        ("P105", 28),
        ("P106", 20),
        ("P107", 41),
        ("P108", 26),
        ("P109", 19),
        ("P110", 34)
    )

    if len(baggage) == 0:
        raise Exception("No baggage data available.")

    baggage_screening(baggage)

except ValueError as e:
    print("Error:", e)

except Exception as e:
    print("Unexpected Error:", e)
