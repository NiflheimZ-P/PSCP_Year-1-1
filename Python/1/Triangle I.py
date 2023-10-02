"""Triangle I"""
def tri():
    """Triangle"""
    most = 0
    cal_1 = 0
    cal_2 = 0
    in_1 = float(input())**2
    in_2 = float(input())**2
    in_3 = float(input())**2
    if in_1 >= in_2 and in_1 >= in_3:
        most = in_1
        cal_1 = in_2
        cal_2 = in_3
    elif in_2 >= in_1 and in_2 >= in_3:
        most = in_2
        cal_1 = in_1
        cal_2 = in_3
    elif in_3 >= in_1 and in_3 >= in_2:
        most = in_3
        cal_1 = in_1
        cal_2 = in_2
    out_1 = ((most)-(cal_1+cal_2))
    if abs(out_1) <= 0.01:
        print("Yes")
    else:
        print("No")
tri()
