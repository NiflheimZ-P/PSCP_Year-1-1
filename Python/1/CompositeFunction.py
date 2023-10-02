"""CompositeFunction"""
def functionx(num_x):
    """FuncX"""
    num_x = int(num_x)
    funcx = num_x*2
    funcg = (num_x/2)+1

    out_1 = funcx*funcg
    out_2 = funcg*funcx
    print(out_1)
    print(out_2)
functionx(input())
