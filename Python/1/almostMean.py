"""AlmostMean"""
def mean():
    """AlmostMean"""
    loops = int(input())
    student_num = []
    score = []
    check = 0
    check_minus = []
    test = []
    count = 0
    for _ in range(loops):
        student_num.append(str(input()).split())
    for i in student_num:
        score.append(float(i.pop(-1)))
        check += (score[-1])
    check /= loops
    for j in score:
        check_minus.append(abs(j-check))
    test = check_minus.copy()
    test.sort()
    for k in check_minus:
        count += 1
        if k == test[0]:
            break
    print("%s\t%s"%(*student_num[count-1], str(score[count-1])))
mean()
