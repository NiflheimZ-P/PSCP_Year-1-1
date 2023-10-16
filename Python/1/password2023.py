"""[Midterm 2023] Password"""
import math
def password(num):
    """[Midterm 2023] Password"""
    entropy = 0
    out_entropy = 0
    if num.isalnum() == False:
        entropy += 32
    for i in num:
        if i.isdigit():
            entropy += 10
            break
    if num.isalnum():
        entropy += 52
        if num.islower():
            entropy -= 26
    out_entropy = int(math.log2(entropy**(len(num))))
    print(out_entropy)
    if out_entropy < 28:
        print("Very Weak")
    elif 28 <= out_entropy < 36:
        print("Weak")
    elif 36 <= out_entropy < 60:
        print("Reasonable")
    elif 60 <= out_entropy < 128:
        print("Strong")
    else:
        print("Very Strong")
password(str(input()))
