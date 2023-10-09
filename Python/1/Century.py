"""[Midterm 2021 + Recommend] Century Home """
def century():
    """[Midterm 2021 + Recommend] Century Home """
    import math as out
    time = int(input())
    check = ""
    count = 0
    bef_or_aft = ""
    for _ in range(time):
        year = str(input())
        for year_out in year:
            count += 1
            if count < 5:
                bef_or_aft += year_out
            elif count >= 6:
                check += year_out
        count = 0
        check = int(check)
        if bef_or_aft == "A.D.":
            print(out.ceil(check/100))
        elif bef_or_aft == "B.E.":
            if check <= 543:
                print("ERROR")
            else:
                check -= 543
                print(out.ceil(check/100))
        else:
            print("ERROR")
        check = ""
        count = 0
        bef_or_aft = ""
century()