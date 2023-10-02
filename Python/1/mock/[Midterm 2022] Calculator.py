"""[Midterm 2022] Calculator"""


def calculator():
    """[Midterm 2022] Calculator"""
    in_1 = int(input())
    count = 0
    if in_1 == 1:
        print("1")
    else:
        for out in range(1, in_1+1):
            out = str(out)
            test = len(out)
            count += (test+1)
        print(count)


calculator()
