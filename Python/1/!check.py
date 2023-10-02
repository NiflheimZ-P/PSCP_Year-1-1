"""[Recommend] Blackjack"""
def blackjack():
    """[Recommend] Blackjack"""
    number_card = int(input())
    score = 0
    ace = 0
    for i in range(number_card):
        i = i
        card = input()
        if card in "JQKjqk":
            score += 10
        elif card in "Aa":
            ace += 1
        else:
            score += int(card)
        while ace > 0:
            ace -= 1
            if score+11 > 21:
                score += 1
            elif score == 10 and ace == 1:
                score += 1
            else:
                score += 11
    print(score)
blackjack()