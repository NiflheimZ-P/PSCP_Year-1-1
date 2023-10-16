"""[Midterm 2023] Password"""
import math
def password(num):
    """[Midterm 2023] Password"""
    entropy = 0
    out_entropy = 0
    low = 0
    alp = 0
    lnum = 0
    able = 0
    if num.islower():
        low = 1
    elif num.isalpha():
        alp = 1
    elif num.isalnum():
        lnum = 1
    elif num.isprintable():
        able = 1
    if low == 1:
        entropy += 26
    if alp == 1:
        entropy += 26
    if lnum == 1:
        entropy += 10
    if able == 1:
        entropy += 32
    out_entropy = int(math.log2(entropy**(len(num))))
    print(out_entropy)
    if out_entropy < 28:
        print("Very Weak")
    elif out_entropy in range(28, 36):
        print("Weak")
    elif out_entropy in range(36, 60):
        print("Reasonable")
    elif out_entropy in range(60, 128):
        print("Strong")
    else:
        print("Very Strong")
password(str(input()))
