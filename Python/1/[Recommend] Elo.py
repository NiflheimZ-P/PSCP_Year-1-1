"""[Recommend] Elo"""
def elo():
    """[Recommend] Elo"""
    rating_a = int(input())
    rating_b = int(input())
    side = str(input())
    if side == "A":
        print("%.2f"%rating_team_a(rating_a, rating_b))
    else:
        print("%.2f"%rating_team_b(rating_a, rating_b))
def rating_team_a(rating_a, rating_b):
    """Find Rating Team A"""
    return 1/((1)+(10**((rating_b-rating_a)/400)))
def rating_team_b(rating_a, rating_b):
    """Find Rating Team B"""
    return 1/((1)+(10**((rating_a-rating_b)/400)))
elo()
