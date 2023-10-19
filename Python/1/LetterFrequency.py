"""LetterFrequency"""
def main(word):
    """LetterFrequency"""
    out = max(list(word), key=list(word).count)
    print(out)
main(input().replace(" ", ""))
