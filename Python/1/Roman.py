"""Roman Number"""
def main(roman):
    """Roman"""
    roman_value = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    out = 0
    for roman_v, value in enumerate(roman):
        if roman_v == len(roman)-1:
            out += roman_value[value]
        elif roman_value[value] >= roman_value[roman[roman_v+1]]:
            out += roman_value[value]
        else:
            out -= roman_value[value]
    print(out)
main(input())
