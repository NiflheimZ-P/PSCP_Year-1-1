"""Key"""


def key():
    """headache mak mak"""
    id_number = str(input())
    count = 0
    last_3_num = 0
    last_3_num = str(last_3_num)
    number = id_number
    sum_number = 0
    for out in number:  # ขั้น 1
        out = int(out)
        sum_number += out
    for out in id_number:  # หา 3 ตัวท้าย
        count += 1
        if 11 <= count < 14:
            last_3_num += out
    last_3_num = int(last_3_num)
    mult_10 = last_3_num*10  # คูณ 10
    last = sum_number+mult_10
    if last >= 10000:
        count = 0
        last = str(last)
        for out in last:
            count += 1
            if count > 1:
                print(out, end="")
        # last_3_num = 0
        # count = 0
        # last = str(last)
        # for out in last:
        #     count += 1
        #     if 2 <= count < 6:
        #         last_3_num = str(last_3_num)
        #         last_3_num += out  # final ans มากกว่า 4 หลัก
        #         count = 0
        #         for out in last_3_num:
        #             count += 1
        #             if count > 1:
        #                 print(out, end="")
    elif last < 1000:
        final = last+1000
        print(final)
    else:
        print(last)


key()
