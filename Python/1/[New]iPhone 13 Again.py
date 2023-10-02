"""Iphone"""


def main():
    """Main"""
    model = str(input())
    storage = str(input())
    if model == "iPhone 13 mini":
        def mini():
            """iPhone 13 mini"""
            if storage == "128 GB":
                print("25900")
            elif storage == "256 GB":
                print("29900")
            elif storage == "512 GB":
                print("37900")
            else:
                print("Not Available")
        mini()
    elif model == "iPhone 13":
        def normal():
            """iPhone 13"""
            if storage == "128 GB":
                print("29900")
            elif storage == "256 GB":
                print("33900")
            elif storage == "512 GB":
                print("41900")
            else:
                print("Not Available")
        normal()
    elif model == "iPhone 13 Pro":
        def pro():
            """iPhone 13 Pro"""
            if storage == "128 GB":
                print("38900")
            elif storage == "256 GB":
                print("42900")
            elif storage == "512 GB":
                print("50900")
            elif storage == "1 TB":
                print("58900")
            else:
                print("Not Available")
        pro()
    elif model == "iPhone 13 Pro Max":
        def promax():
            """iPhone 13 Pro Max"""
            if storage == "128 GB":
                print("42900")
            elif storage == "256 GB":
                print("46900")
            elif storage == "512 GB":
                print("54900")
            elif storage == "1 TB":
                print("62900")
            else:
                print("Not Available")
        promax()
    else:
        print("Not Available")


main()
