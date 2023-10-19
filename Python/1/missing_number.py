"""Ejudge"""
def main():
    """MissingNumber"""
    num = int(input())
    listnum = []
    while True:
        numtmp = int(input())
        listnum.append(numtmp)
        if numtmp == 0:
            break
    listnum.sort()
    for i in range(1, num+1):
        if i not in listnum:
            print(i)
main()
