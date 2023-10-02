"""HideAndSeek"""
def main():
    """HideAndSeek"""
    start = int(input())
    stop = int(input())
    step = int(input())
    if stop == 0:
        print("")
    elif start > stop:
        for number in range(start, stop-1, -step):
            print(number)
    else:
        for number in range(start, stop, step):
            print(number)
main()
