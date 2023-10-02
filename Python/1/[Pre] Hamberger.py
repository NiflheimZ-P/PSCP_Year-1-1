"""HamSter"""
def main():
    """Ahemm"""
    left = int(input())
    right = int(input())
    meat = (left + right)*2
    out_1 = ("|"*left)
    out_2 = ("|"*right)
    meat = ("*"*meat)
    print(out_1+meat+out_2)
main()
