"""Digit v2"""
def main(word):
    """Digit v2"""
    zerotonine = ["zero", "one", "two", "three", "four", "five", "six", "seven"\
                  , "eight", "nine"]
    if "thousand" in word:
        print("4")
    elif "hundred" in word:
        print("3")
    elif word in zerotonine:
        print("1")
    else:
        print("2")
main(input())
