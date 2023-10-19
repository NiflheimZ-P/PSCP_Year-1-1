"""Easy Histogram"""
def sort_out(in_1):
    """Easy Histogram"""
    if in_1.isupper():
        return ord(in_1.lower())+0.5
    else:
        return ord(in_1)
def main():
    """Easy Histogram"""
    in_1 = input()
    out = {}
    for i in in_1:
        if i.isalpha():
            out[i] = out.get(i, 0) + 1
    list_out = list(out)
    list_out.sort(key=sort_out)
    for j in list_out:
        print(j, "=", out[j])
main()
