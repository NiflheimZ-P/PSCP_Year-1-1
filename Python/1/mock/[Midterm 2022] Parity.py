"""[Midterm 2022] Parity"""


def parity():
    """[Midterm 2022] Parity"""
    data = str(input())
    ev_or_od = str(input())
    count = 0
    for out in data:
        if out == "1":
            count += 1
    check = count % 2
    if ev_or_od == "Even":
        if check == 1:
            print(data+"1")
        else:
            print(data+"0")
    else:
        if check == 1:
            print(data+"0")
        else:
            print(data+"1")


parity()
