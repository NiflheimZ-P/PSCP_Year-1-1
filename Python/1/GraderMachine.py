"""GraderMachine"""
def main():
    """MaiRuu Kid mai ook la"""
    start = int(input())
    stop = int(input())
    sum_num = 0
    print("pass :", end="")
    for test in range(start+1, stop+1, 2):
        print("", test, end="")
        sum_num += test
    print("\n", end="")
    print("Sum :", sum_num)
main()
