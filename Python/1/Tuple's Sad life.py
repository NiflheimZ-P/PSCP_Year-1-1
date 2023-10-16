"""Tuple's Sad life"""
def sad():
    """Tuple's Sad life"""
    count = 0
    test = input()
    want = input()
    out = ()
    for i in test:
        count += 1
        if count%2 == 1:
            out += tuple(i)
    time = out.count(want)
    for j in range(time):
        for _ in range(time):
            print(out.index(want), "",end="")
        print()
sad()
