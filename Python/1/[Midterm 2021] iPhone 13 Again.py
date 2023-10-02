"""[Midterm 2021] iPhone 13 Again"""


def iphone():
    """[Midterm 2021] iPhone 13 Again"""
    model = str(input())
    storage = str(input())
    if storage == "128 GB":
        if model == "iPhone 13 mini":
            print("25900")
        elif model == "iPhone 13":
            print("29900")
        elif model == "iPhone 13 Pro":
            print("38900")
        elif model == "iPhone 13 Pro Max":
            print("42900")
        else:
            print("Not Available")
    elif storage == "256 GB":
        if model == "iPhone 13 mini":
            print("29900")
        elif model == "iPhone 13":
            print("33900")
        elif model == "iPhone 13 Pro":
            print("42900")
        elif model == "iPhone 13 Pro Max":
            print("46900")
        else:
            print("Not Available")
    elif storage == "512 GB":
        if model == "iPhone 13 mini":
            print("37900")
        elif model == "iPhone 13":
            print("41900")
        elif model == "iPhone 13 Pro":
            print("50900")
        elif model == "iPhone 13 Pro Max":
            print("54900")
        else:
            print("Not Available")
    elif storage == "1 TB":
        if model == "iPhone 13 Pro":
            print("58900")
        elif model == "iPhone 13 Pro Max":
            print("62900")
        else:
            print("Not Available")
    else:
        print("Not Available")


iphone()
