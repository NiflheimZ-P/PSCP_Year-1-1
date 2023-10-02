"""Stepper I"""
def main():
    """Stepper I"""
    start = int(input())
    stop = int(input())
    if start > stop:
        for number in range(start, stop-1, -1):
            print(number)
    else:
        for number in range(start, stop+1, 1):
            print(number)
main()
