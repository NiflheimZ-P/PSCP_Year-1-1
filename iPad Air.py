"""iPad Air"""
def ipad():
    """Ipad"""
    color = ["Space Gray", "Silver", "Green", "Rose Gold", "Sky Blue"]
    input_color = str(input())
    storage = int(input())
    internet = str(input())
    if input_color in color:
        if storage == 64:
            if internet == "Wi-Fi":
                print("19900")
            elif internet == "Wi-Fi + Cellular":
                print("24400")
            else:
                print("Not Available")
        elif storage == 256:
            if internet == "Wi-Fi":
                print("24900")
            elif internet == "Wi-Fi + Cellular":
                print("29400")
            else:
                print("Not Available")
        else:
            print("Not Available")
    else:
        print("Not Available")
ipad()
