"""[Midterm 2023] Lift"""
def lift():
    """[Midterm 2023] Lift"""
    people = int(input())
    weight_lift = float(input())
    all_weight = 0
    less_12 = 0
    more_12 = 0
    for _ in range(people):
        age = int(input())
        weight = float(input())
        all_weight += weight
        if age >= 12:
            more_12 += 1
        elif age < 12:
            less_12 += 1
    if weight_lift >= all_weight:
        if less_12 >= 1 and more_12 >= 1:
            print("Safe")
        elif less_12 >= 1 and more_12 < 1:
            print("Not Safe")
        else:
            print("Safe")
    else:
        print("Not Safe")
lift()
