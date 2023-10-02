"""SurprisingVote"""
def vote(total, highest):
    """SurprisingVote"""
    lowest = total - (highest*2)
    check = max(lowest, 0)
    if abs(highest - check) > 2:
        print("Surprising")
    else:
        print("Not surprising")
vote(float(input()), float(input()))
