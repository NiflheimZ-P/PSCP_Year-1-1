"""[Midterm 2023] Bad Keyboard"""
def bad():
    """[Midterm 2023] Bad Keyboard"""
    word = str(input())
    new_word = ""
    for i in word:
        if i == "i":
            new_word += "o"
        elif i == "I":
            new_word += "O"
        elif i == "o":
            new_word += "i"
        elif i == "O":
            new_word += "I"
        else:
            new_word += i
    print(new_word)
bad()
