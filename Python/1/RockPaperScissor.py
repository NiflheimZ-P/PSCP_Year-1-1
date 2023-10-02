"""RockPaperScissor"""


def rps():
    """RockPaperScissor"""
    word = str(input())
    count = 0
    check = ""
    a_score = 0
    b_score = 0
    for out in word:
        count += 1
        check += out
        if count == 2:
            count = 0
            if check == "PR":  # นับแต้ม P1
                a_score += 1
            elif check == "RS":
                a_score += 1
            elif check == "SP":
                a_score += 1
            elif check == "RP":  # นับแต้ม P2
                b_score += 1
            elif check == "SR":
                b_score += 1
            elif check == "PS":
                b_score += 1
            check = ""
    if a_score > b_score:
        print("A win %d-%d" % (a_score, b_score))
    elif a_score < b_score:
        print("B win %d-%d" % (b_score, a_score))
    else:
        print("DRAW %d" % a_score)


rps()
