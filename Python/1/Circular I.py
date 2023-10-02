'''Circular I'''

def circular():
    """Circular I"""
    in_x = float(input())
    in_y = float(input())
    in_r = float(input())
    in_xn = float(input())
    in_yn = float(input())

    test = (((in_xn - in_x)**2)+((in_y - in_yn)**2))**0.5
    if test <= in_r:
        print("Yes")
    else:
        print("No")
circular()
