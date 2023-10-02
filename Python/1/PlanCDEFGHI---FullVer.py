"""Too long"""
def main():
    """PlanCDEFGHIJKLMNOPQRSTUVWXYZ"""
    option = input()
    num_1 = float(input())
    num_2 = float(input())
    num_3 = float(input())
 
    if option == "Ascend":
        def ascend():
            """Ascend"""
            out_1 = 0
            out_2 = 0
            out_3 = 0
            if num_1 >= num_2 and num_1 >= num_3:
                out_1 = num_1
                if num_2 >= num_3:
                    out_2 = num_2
                    out_3 = num_3
                else:
                    out_2 = num_3
                    out_3 = num_2
            if num_2 >= num_1 and num_2 >= num_3:
                out_1 = num_2
                if num_1 >= num_3:
                    out_2 = num_1
                    out_3 = num_3
                else:
                    out_2 = num_3
                    out_3 = num_1
            if num_3 >= num_1 and num_3 >= num_2:
                out_1 = num_3
                if num_1 >= num_2:
                    out_2 = num_1
                    out_3 = num_2
                else:
                    out_2 = num_2
                    out_3 = num_1
            print("%.2f, %.2f, %.2f" %(out_3, out_2, out_1))
        ascend()
    else:
        def descend():
            """descend"""
            out_1 = 0
            out_2 = 0
            out_3 = 0
            if num_1 >= num_2 and num_1 >= num_3:
                out_1 = num_1
                if num_2 >= num_3:
                    out_2 = num_2
                    out_3 = num_3
                else:
                    out_2 = num_3
                    out_3 = num_2
            if num_2 >= num_1 and num_2 >= num_3:
                out_1 = num_2
                if num_1 >= num_3:
                    out_2 = num_1
                    out_3 = num_3
                else:
                    out_2 = num_3
                    out_3 = num_1
            if num_3 >= num_1 and num_3 >= num_2:
                out_1 = num_3
                if num_1 >= num_2:
                    out_2 = num_1
                    out_3 = num_2
                else:
                    out_2 = num_2
                    out_3 = num_1
            print("%.2f, %.2f, %.2f" %(out_1, out_2, out_3))
        descend()
main()
