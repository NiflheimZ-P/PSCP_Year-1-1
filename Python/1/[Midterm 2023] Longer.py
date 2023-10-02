"""[Midterm 2023] Longer"""
import math
def longer():
    """[Midterm 2023] Longer"""
    radius = float(input())
    in_a = float(input())
    in_b = float(input())
    circle = (2*math.pi)*radius
    square = (in_a+in_b)*2
    diff = abs(circle-square)
    if circle > square:
        print("Circle is longer")
    elif circle < square:
        print("Rectangle is longer")
    else:
        print("Equal")
    print("%.5f"%diff)
longer()
