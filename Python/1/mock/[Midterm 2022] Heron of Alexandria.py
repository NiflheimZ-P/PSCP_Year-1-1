"""[Midterm 2022] Heron of Alexandria"""


def main():
    """[Midterm 2022] Heron of Alexandria"""
    in_a = float(input())
    in_b = float(input())
    in_c = float(input())
    s_cal = (in_a+in_b+in_c)/2
    area = (s_cal*((s_cal-in_a)*(s_cal-in_b)*(s_cal-in_c)))**0.5
    print("%.3f" % area)


main()
