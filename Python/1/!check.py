"""Tuple's Sad life"""
def sad():
    """Tuple's Sad life"""
    test = tuple(input().split())
    want = input()
    time = test.count(want)
    for _ in range(time):
        for _ in range(time):
            print(test.index(want), "", end="")
        print()
sad()
