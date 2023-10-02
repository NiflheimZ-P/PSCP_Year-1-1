"""Align"""


def main():
    """Align"""
    size = int(input())
    location = str(input())
    word = str(input())
    space = len(word)
    free_space = size - space
    if location == "left":
        print(word+(" "*free_space))
    elif location == "center":
        if free_space % 2 == 0:
            test = word.center(size, " ")
            print(test)
        else:
            test = word.center(size+1, " ")
            print(test)
    elif location == "right":
        print((" "*free_space)+word)


main()
