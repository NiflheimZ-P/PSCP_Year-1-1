"""Heads and Legs"""
def main():
    """Heads and Legs"""
    animal = int(input())
    leg = int(input())
    rabbit, nodisable = divmod(leg-2*animal, 2)
    bird = animal - rabbit
    if bird >= 0 and rabbit >= 0 and nodisable == 0:
        print(rabbit, bird)
    else:
        print("Impossible")
main()
