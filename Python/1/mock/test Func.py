"""Test"""


def main():
    """Test Function"""
    in_x = float(input())
    in_y = float(input())
    in_z = float(input())
    print("Test %.2f %.2f %.2f" % (cal_x(in_x), cal_y(in_x, in_y), cal_z()))


def cal_x(in_x):
    """Test Cal_X"""
    cal_1 = (in_x**2)
    print(cal_1)
    return cal_1


def cal_y(in_x, in_y):
    """Test Cal_Y"""
    cal_2 = (in_x/2)*in_y
    print(cal_2)
    return cal_2


def cal_z(cal_x, cal_y):
    """Test Cal_Z"""
    cal_3 = (cal_x+cal_y)


main()
