"""Robot"""
def agecheck():
    """Age"""
    name = input()
    age = float(input())
    if age < 18:
        print("%s, you can pass."%name)
    else:
        print("%s, you shall not pass."%name)


agecheck()
