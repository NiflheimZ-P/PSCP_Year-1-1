"""isprime_small"""
def prime(number):
    """isprime_small"""
    out = 0
    if number > 1:
        for i in range(2, (number//2)+1):
            if number%i == 0:
                out += 0
        else:
            out += 1
    else:
        out = 0
    print(out)
prime(int(input()))