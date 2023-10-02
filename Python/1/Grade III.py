"""Grade"""
import math


def table():
    """Ta lang kra nan"""
    point = int(input())
    sum_point = 0
    for _ in range(point):
        score = float(input())
        if 95 <= score <= 100:
            sum_point += 4
        elif 90 <= score < 95:
            sum_point += 3.5
        elif 85 <= score < 90:
            sum_point += 3
        elif 80 <= score < 85:
            sum_point += 2.5
        elif 75 <= score < 80:
            sum_point += 2
        elif 70 <= score < 75:
            sum_point += 1.5
        elif 65 <= score < 70:
            sum_point += 1
        elif 60 <= score < 65:
            sum_point += 0.5
        elif 0 <= score < 60:
            sum_point += 0
    grade = sum_point/point
    minus = math.floor(grade)
    cal_1 = grade - minus
    cal_1 = cal_1*100
    cal_1 = math.floor(cal_1)
    cal_1 = cal_1/100
    grade = minus + cal_1
    print("%.2f" % grade)


table()
