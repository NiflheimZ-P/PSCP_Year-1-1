"""[Midterm 2022] Meteorite"""


def meteorite():
    """[Midterm 2022] Meteorite"""
    weight_m = float(input())
    fragment_m = int(input())
    wei_can_des = float(input())
    test = 0
    if weight_m >= wei_can_des:
        avg_wei = (weight_m/fragment_m)
        count = 1
        while avg_wei > wei_can_des:
            avg_wei = (avg_wei/fragment_m)
            count += 1
            if avg_wei <= wei_can_des:
                break
        for out in range(0, count):
            test += (fragment_m**out)
        print(test)
    else:
        print("0")


meteorite()
