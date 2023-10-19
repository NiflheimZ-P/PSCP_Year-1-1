"""HorizontalHistogram"""
def histogram(var):
    """HorizontalHistogram"""
    char = var[0]
    return ord(char) + (100 if char.isupper() else 0)
def main(string):
    """HorizontalHistogram"""
    for char, text in sorted({i : string.count(i) for i in string}.items(), key=histogram):
        print(char, ":", "".join(["-" if i % 5 else "-|" for i in range(1, text+1)]).rstrip("|"))
main(input())
