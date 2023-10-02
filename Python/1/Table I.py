"""Table I"""


def table():
    """Ta lang sude koon mae 15"""
    tuakoon = int(input())
    ponkoon = 0
    for out in range(1, tuakoon+1):
        ponkoon = 15*out
        print("15 x %d = %d" % (out, ponkoon))


table()
