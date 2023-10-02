"""Seven"""


def seven():
    """Seven"""
    in_1 = int(input())
    check = in_1 % 4
    if check == 1:
        print("7")
    elif check == 2:
        print("9")
    elif check == 3:
        print("3")
    else:
        print("1")


seven()
