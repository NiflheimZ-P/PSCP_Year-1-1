"""[Midterm 2023] Bonus"""
def bonus():
    """[Midterm 2023] Bonus"""
    salary = int(input())
    years = int(input())
    month = int(input())
    if month >= 10:
        years += 1
    if years >= 20:
        years = 20
    new_bonus = salary*years
    if new_bonus > 1000000:
        new_bonus = 1000000
    elif new_bonus < 5000:
        new_bonus = 5000
    print(new_bonus)
bonus()
