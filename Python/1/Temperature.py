"""Temperature"""
def temp():
    """Temperature"""
    temperature = float(input())
    rightnow = input()
    want = input()
    if rightnow == "R":
        temperature = (temperature/(9/5))-273.15
    elif rightnow == "K":
        temperature = temperature-273.15
    elif rightnow == "F":
        temperature = (temperature-32)/(9/5)
    if want == "F":
        print("%.2f"%((temperature*(9/5))+32))
    elif want == "K":
        print("%.2f"%(temperature+273.15))
    elif want == "R":
        print("%.2f"%((temperature+273.15)*(9/5)))
    else:
        print("%.2f"%temperature)
temp()
