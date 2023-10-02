"""Largest Number"""
def main():
    """Largest Number"""
    in_1 = int(input())
    in_2 = int(input())
    in_3 = int(input())
    most = 0
    mid = 0
    less = 0
    if in_2 <= in_1 >= in_3:
        most = in_1
        if in_2 >= in_3:
            mid = in_2
            less = in_3
        else:
            mid = in_3
            less = in_2
    elif in_1 <= in_2 >= in_3:
        most = in_2
        if in_1 >= in_3:
            mid = in_1
            less = in_3
        else:
            mid = in_3
            less = in_1
    elif in_2 <= in_3 >= in_1:
        most = in_3
        if in_2 >= in_1:
            mid = in_2
            less = in_1
        else:
            mid = in_1
            less = in_2
    print("%d%d%d"%(most, mid, less))

main()
