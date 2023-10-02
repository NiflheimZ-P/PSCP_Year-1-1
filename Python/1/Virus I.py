"""Virus I"""


def virus():
    """Virus I"""
    text = str(input())
    count = 0
    for out in text:
        if out == "o":
            count += 1
    print(count)


virus()
