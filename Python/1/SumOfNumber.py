"""SumOfNumber"""


def main():
    """SumOfNumber"""
    stop_point = int(input())
    cal_1 = 0
    while True:
        in_1 = int(input())
        if in_1 == -1:
            break
        cal_1 = cal_1+in_1
        if cal_1 == stop_point:
            break
        if in_1 == -1:
            break
    print(cal_1)


main()
