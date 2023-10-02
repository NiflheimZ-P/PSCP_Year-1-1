"""[Midterm 2020] BigFrame"""
def big():
    """Frame"""
    word_1 = str(input()).strip()
    word_2 = str(input()).strip()
    word_3 = str(input()).strip()
    word_4 = str(input()).strip()
    word_5 = str(input()).strip()
    len_w_1 = len(word_1)
    len_w_2 = len(word_2)
    len_w_3 = len(word_3)
    len_w_4 = len(word_4)
    len_w_5 = len(word_5)
    space_max = max(len_w_1, len_w_2, len_w_3,\
                    len_w_4, len_w_5)
    space = ("*"*(space_max+4))
    print(space)
    print("*", word_1.ljust(space_max), "*")
    print("*", word_2.ljust(space_max), "*")
    print("*", word_3.ljust(space_max), "*")
    print("*", word_4.ljust(space_max), "*")
    print("*", word_5.ljust(space_max), "*")
    print(space)
big()
