"""Difference"""
def diff(a_member, b_member):
    """Difference"""
    set_a = set()
    set_b = set()
    for _ in range(a_member):
        set_a.add(int(input()))
    for _ in range(b_member):
        set_b.add(int(input()))
    print(*(sorted(set_a.difference(set_b))))
diff(int(input()), int(input()))
