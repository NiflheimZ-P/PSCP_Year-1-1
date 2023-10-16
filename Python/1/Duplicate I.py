"""Duplicate I"""
def duplicate():
    """Duplicate I"""
    group_1_member = int(input())
    group_2_member = int(input())
    group_1 = set([int(input())for _ in range(group_1_member)])
    group_2 = set([int(input())for _ in range(group_2_member)])
    out = (group_1.intersection(group_2))
    if out == set():
        print("Nope")
    else:
        out = sorted(out, reverse=True)
        for i in out:
            print(i)
duplicate()
