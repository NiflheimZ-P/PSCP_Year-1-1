"""[Midterm 2023] Password"""
import math
def password(num):
    """[Midterm 2023] Password"""
    entropy = 0
    out_entropy = 0
    if num.islower():
        entropy = 26
    if num.isalpha():
        entropy = 52
    if num.isalnum():
        entropy = 62
    if num.isprintable():
        entropy = 94
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
