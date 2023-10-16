"""NumDays"""
def days():
    """NumDays"""
    month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    firstday = int(input())
    firstmonth = int(input())
    lastday = int(input())
    lastmonth = int(input())
    if firstmonth < lastmonth:
        def normal(month, firstday, firstmonth, lastmonth, lastday):
            """Holy"""
            final = 0
            for i in range(firstmonth, lastmonth+1):
                if i == firstmonth:
                    if month[i] < firstday:
                        final = "Impossible"
                        break
                    final += month[i]-firstday
                elif i == lastmonth:
                    if  month[i] < lastday:
                        final = "Impossible"
                        break
                    final += lastday
                else:
                    final += month[i]
            return final
        print(normal(month, firstday, firstmonth, lastmonth, lastday))
    elif firstmonth > lastmonth:
        def unnormal(month, firstday, firstmonth, lastmonth, lastday):
            """Papsi"""
            final = 0
            for i in range(lastmonth, firstmonth-1, -1):
                if i == firstmonth:
                    if month[i] < firstday:
                        final = "Impossible"
                        break
                    final += month[i]-firstday
                elif i == lastmonth:
                    if  month[i] < lastday:
                        final = "Impossible"
                        break
                    final += lastday
                else:
                    final += month[i]
            return final
        print(unnormal(month, firstday, firstmonth, lastmonth, lastday))
    else:
        def equl(month, firstday, firstmonth, lastmonth, lastday):
            """equal"""
            final = 0
            if firstday > month[firstmonth]:
                final = "Impossible"
            elif lastday > month[lastmonth]:
                final = "Impossible"
            elif  firstday > lastday:
                final = firstday - lastday
            else:
                final = lastday - firstday
            return final
        print(equl(month, firstday, firstmonth, lastmonth, lastday))
days()
