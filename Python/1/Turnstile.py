"""Turnstile"""
def turnstile():
    """Turnstile"""
    point = 0
    count = 0
    while True:
        word = str(input())
        if word == "END":
            break
        if word == "P":
            if point == 0:
                point = 0
            elif point == 1:
                point = 0
                count += 1
        elif word == "C":
            if point == 0:
                point = 1
            elif point == 1:
                point = 1
    print(count)



turnstile()
