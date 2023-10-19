"""Easy Histogram (No Dict)"""
def main(word):
    """Easy Histogram (No Dict)"""
    if word.isupper():
        check = ord(word) - ord("A")
    else:
        check = ord(word) - ord("a")
    return check, word.isupper()
def histogram(char):
    """Easy Histogram (No Dict)"""
    out = []
    for i in char:
        if i not in out and i != " ":
            out.append(i)
    out.sort(key=main)
    for j in out:
        print("{} = {}".format(j, char.count(j)))
histogram(tuple(input()))
