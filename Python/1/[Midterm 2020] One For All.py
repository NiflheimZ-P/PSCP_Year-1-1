"""[Midterm 2020] One For All"""
def one():
    """[Midterm 2020] One For All"""
    time = int(input())
    count = 0
    out = ""
    for _ in range(time):
        count += 1
        name = input()
        if count == time:
            out += name+"_"+str(count)
        elif count%2 == 0:
            # print("%s%s"%(name, ("*"*count)),end="")
            out += name+("-"*count)
        else:
            # print("%s%s"%(name, ("-"*count)), end="")
            out += name+("*"*count)
    print(out)
one()
