"""Hamburger"""


def ham():
    """R U Hungry"""
    left = int(input())
    right = int(input())
    bread = left+right
    meat = (bread*2)*"*"
    left = ("|"*left)
    right = ("|"*right)
    print(left+meat+right)


ham()
