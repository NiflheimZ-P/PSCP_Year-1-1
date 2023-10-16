"""BloodDonation"""
def main():
    """Main"""
    age = int(input())
    weight = int(input())
    time = int(input())
    if age == 17 or 60 <= age <= 70:
        agree = str(input())
    if weight_check == True:
        if age == 17 or 60 <= age <= 70:
            if time >= 1:
                if agree_check == True:
                    return True
                else:
                    return False
            elif time == 0 and 17 <= age <= 55:
                if agree_check == True:
                    return True
                else:
                    return False
            else:
                return False
        elif 17 <= age <= 70:
            if age <= 55 :
                return True
            elif age > 55 and time > 0:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
def weight_check(weight):
    """Weight Check"""
    if weight >= 45:
        return True
    else:
        return False
def agree_check(agree):
    """Agree Check"""
    if agree == "True":
        return True
    else:
        return False
print(main())
