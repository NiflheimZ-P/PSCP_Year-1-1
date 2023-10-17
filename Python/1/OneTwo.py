"""OneTwo"""
def one(time):
    """OneTwo"""
    seq_1 = ""
    seq_2 = "2"
    seq_n = ""
    count = 0
    if time > 0:
        for _ in range(time-2):
            count += 1
            if count%2 == 0:
                seq_1 += "2"
            else:
                seq_1 += "1"
            seq_n = seq_2+seq_1
            seq_2 = seq_n
        print(seq_n)
    else:
        if time == 2:
            print("2")
        elif time == 1:
            print("1")
one(int(input()))
