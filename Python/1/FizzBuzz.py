"""FizzBuzz"""


def game():
    """mai keay len naa"""
    number = int(input())
    for out in range(1, number+1):
        if out % 3 == 0 and out % 5 == 0:
            print("FizzBuzz")
        elif out % 3 == 0:
            print("Fizz")
        elif out % 5 == 0:
            print("Buzz")
        else:
            print(out)


game()
