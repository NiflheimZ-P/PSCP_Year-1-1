"""[Midterm 2021] Squid Game"""


def squid():
    """[Midterm 2021] Squid Game"""
    count = 0
    team_a = 0
    team_b = 0
    for _ in range(20):
        power = int(input())
        count += 1
        if count < 11:
            team_a += power
        else:
            team_b += power
    if team_a > team_b:
        print("B")
    elif team_b > team_a:
        print("A")
    else:
        print("AB")


squid()
