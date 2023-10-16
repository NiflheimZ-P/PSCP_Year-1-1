"""Seeker"""
def seeker():
    """Seeker"""
    word = input()
    check = 0
    out = 0
    for i in word:
        if i.isdecimal():
            check = str(check)
            check += i
        else:
            out += int(check)
            check = 0
    out += int(check)
    print(out)
seeker()
