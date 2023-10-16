"""Ejudge"""
import hashlib
def main():
    """password"""
    word = hashlib.sha512(input().encode('utf-8'))
    print(word.hexdigest().upper())
main()
