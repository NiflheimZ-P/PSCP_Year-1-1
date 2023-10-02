"""FOR!F-Ball"""
def ball():
    """FOR!F-Ball"""
    word = str(input())
    swappoint = 1
    for check in word:
        if check == "A":
            if swappoint == 1:
                swappoint = 2
            elif swappoint == 2:
                swappoint = 1
        elif check == "B":
            if swappoint == 2:
                swappoint = 3
            elif swappoint == 3:
                swappoint = 2
        elif check == "C":
            if swappoint == 3:
                swappoint = 1
            elif swappoint == 1:
                swappoint = 3
    print(swappoint)
ball()
