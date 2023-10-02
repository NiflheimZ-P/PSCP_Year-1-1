"""[Midterm 2023] Niwarn World"""
import math
def niwarn():
    """[Midterm 2023] Niwarn World"""
    in_n = float(input())
    in_s = float(input())
    in_k = float(input())
    print("X: %.1f, Y: %.1f, Z: %.1f"%(cal_x(in_n), cal_y(in_n, in_s), cal_z(in_k)))
def cal_x(in_n):
    """find X"""
    return 2+((math.log2(in_n**2))/((2*in_n)*(math.log2(in_n))))
def cal_y(in_n, in_s):
    """find Y"""
    check_y = ((math.sin(math.radians(30))+math.sqrt(2*in_s))/(cal_x(in_n)+3))
    return check_y
def cal_z(in_k):
    """find Z"""
    check_z = (((cal_y(in_k, in_k))**2)+(((8456*(cal_x(in_k))**4))/(24*in_k)))
    return check_z

niwarn()
