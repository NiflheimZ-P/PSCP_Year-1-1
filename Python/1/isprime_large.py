"""isPrime_large"""
def prime(number):
    """isPrime_large"""
    if number > 1:
        for i in range(2, int(number**0.5)+1):
            if number%i == 0:
                print("NO")
                break
        else:
            print("YES")
    else:
        print("NO")
prime(int(input()))
