"""Ejudge"""


def main():
    """Left Arrow"""
    kwang = int(input())
    height = int(input())
    tmp = int(height/2)
    for i in range(height):
        if i < height//2:
            print(" "*(tmp)+"*"*kwang)
            tmp -= 1
        else:
            if tmp < 0:
                tmp = 0
            print(" "*(tmp)+"*"*kwang)
            tmp += 1


main()
