"""2inary"""
def inary(number):
    """2nary"""
    out = ""
    if number == 0:
        print("0")
    else:
        while number > 0:
            sage = number%2
            out += str(sage)
            number //= 2
        print(out[::-1])
inary(abs(int(input())))
