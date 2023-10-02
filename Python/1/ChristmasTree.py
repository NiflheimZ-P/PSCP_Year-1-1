"""ChristmasTree"""


def christmas():
    """ChristmasTree"""
    leaf = int(input())
    wood = int(input())
    space = 1
    bai = "*"
    mai = "---"
    for _ in range(1, leaf):  # หาSpace
        space += 2
    for out in range(1, space+1, 2):
        test = bai*out
        print(test.center(space, " "))
    for out in range(1, wood+1):
        print(mai.center(space, " "))


christmas()
