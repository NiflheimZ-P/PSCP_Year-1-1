"""Sequence VII"""


def sequence():
    """Sequence VII"""
    in_1 = int(input())
    for out in range(1, in_1+1):
        for test in range(1, out+1):
            print(test, "", end="")
        print()


sequence()
