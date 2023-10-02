"""Frame"""


def frame():
    """Frame"""
    word = str(input())
    space = len(word)
    space += 2
    space = ("*"*space)
    print(space)
    print("*%s*" % word)
    print(space)


frame()
