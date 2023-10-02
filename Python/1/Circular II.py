'''Circular II'''

def circular():
    """Circular II"""
    in_x = float(input())
    in_y = float(input())
    in_r_1 = float(input())
    in_xn = float(input())
    in_yn = float(input())
    in_r_2 = float(input())
    dis = (((in_xn - in_x)**2)+((in_y - in_yn)**2))**0.5
    sum_r = in_r_1+in_r_2
    if dis < sum_r:
        print("Yes")
    else:
        print("No")
circular()
