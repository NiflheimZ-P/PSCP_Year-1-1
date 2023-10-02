"""BMIAgain"""
def main():
    """BMI"""
    weight = int(input())
    hight = int(input())/100
    bmi = (weight/hight**2)
    if bmi < 18.5:
        print("Underweight")
    elif 18.5 <= bmi < 25:
        print("Normal")
    elif 25 <= bmi < 30:
        print("Overweight")
    else:
        print("Obese")

main()
