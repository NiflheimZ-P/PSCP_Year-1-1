"""Ejudge"""
def main():
    """Cat Parade"""
    cats = []
    saipan = []
    while True:
        word = input()
        if word == "END":
            break
        elif word != "IT'S A DOG":
            for cat in word.split(","):
                cats.append(cat.strip())
                if saipan.count(cat.strip()) == 0:
                    saipan.append(cat.strip())
        elif word == "IT'S A DOG":
            cats.pop()
            saipan.pop()
    saipan.sort()
    for cat in saipan:
        print(cat, cats.index(cat) + 1, cats.count(cat))
main()
