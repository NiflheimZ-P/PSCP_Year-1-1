"""Ejudge"""
def main():
    """AlmostMean"""
    nisit = []
    scorenisit = []
    scoresum = 0
    numnisit = int(input())
    for _ in range(numnisit):
        tmp = input().split()
        nisit.append(tmp[0])
        scorenisit.append(float(tmp[1]))
        tmp = []
    for i in scorenisit:
        scoresum += float(i)
    mean = scoresum/numnisit
    scoresort = sorted(scorenisit)
    indexscore = 0
    while True:
        if float(scoresort[indexscore]) >= mean:
            indexscore -= 1
            break
        indexscore += 1
    for i in range(len(scorenisit)):
        if float(scorenisit[i]) == float(scoresort[indexscore]):
            print("%s\t%s"%(nisit[i], str(scorenisit[i])))
main()
