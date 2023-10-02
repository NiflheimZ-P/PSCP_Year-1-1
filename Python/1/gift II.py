"""Gift II"""
def main():
    """Test"""
    in_1 = int(input())
    in_2 = int(input())
    in_3 = int(input())
    in_4 = int(input())
    in_5 = int(input())
    in_6 = int(input())
    in_7 = int(input())
    in_8 = int(input())
    def check():
        """check"""
        ch_1 = in_1%2
        ch_2 = in_2%2
        ch_3 = in_3%2
        ch_4 = in_4%2
        ch_5 = in_5%2
        ch_6 = in_6%2
        ch_7 = in_7%2
        ch_8 = in_8%2
        if ch_1 == 0:
            print(in_1)
        elif ch_2 == 0:
            print(in_2)
        elif ch_3 == 0:
            print(in_3)
        elif ch_4 == 0:
            print(in_4)
        elif ch_5 == 0:
            print(in_5)
        elif ch_6 == 0:
            print(in_6)
        elif ch_7 == 0:
            print(in_7)
        elif ch_8 == 0:
            print(in_8)
    check()
main()
