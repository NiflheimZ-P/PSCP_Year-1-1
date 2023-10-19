"""Ejudge"""
def main():
    """AndAgainAndAgainAndAgainAndAgainAndAgainAndAgain"""
    ans = []
    word = input().replace(".", "")
    wordlist = word.split()
    for i in wordlist:
        total = i.count("a") + i.count("e") + i.count("i") + i.count("o") + i.count("u")
        if total >= 2:
            ans.append(i)
    ans.sort()
    if len(ans) == 0:
        print("Nope")
    else:
        for i in ans:
            print(i)
main()
