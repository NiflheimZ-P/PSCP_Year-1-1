"""Ejudge"""
import json
def main():
    """Filter"""
    dictscore = json.loads(input())
    socre = float(input())
    ans = []
    for i in dictscore:
        if dictscore[i] >= socre:
            ans.append(i)
    if len(ans) == 0:
        print("Nope")
    else:
        for i in sorted(ans):
            print("%s\t%.2f"%(i, dictscore[i]))
main()
