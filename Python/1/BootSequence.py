"""BootSequence"""


def boost():
    """BootSequence"""
    time = int(input())
    count = 0
    for out in range(1, time+1):
        print("%d" % out, end="")
        for _ in range(1):
            count += 1
            if count == time:
                break
            print("_", end="")


boost()
