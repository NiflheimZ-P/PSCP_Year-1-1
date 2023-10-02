"""WeightStation"""
def main():
    """Weight"""
    avg_wei = float(input())
    wei_1 = float(input())
    wei_2 = float(input())
    wei_3 = float(input())
    wei_4 = (avg_wei*4) - (wei_1+wei_2+wei_3)
    half_avg = avg_wei/2

    if (avg_wei*4) > 15000:
        print("Overweight")
    elif (avg_wei - half_avg) > wei_1 or (avg_wei + half_avg)\
    < wei_1:
        print("Unbalance")
    elif (avg_wei - half_avg) > wei_2 or (avg_wei + half_avg)\
    < wei_2:
        print("Unbalance")
    elif (avg_wei - half_avg) > wei_3 or (avg_wei + half_avg)\
    < wei_3:
        print("Unbalance")
    elif (avg_wei - half_avg) > wei_4 or (avg_wei + half_avg)\
    < wei_4:
        print("Unbalance")
    else:
        print("Pass %.2f" %wei_4)
main()
