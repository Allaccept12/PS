


def isPalindrome(s):
    s = "".join(e for e in s if e.isalnum()).lower()
    #슬라이스를 활용해 리스트를 뒤집어 비교한다
    return s == s[::-1]




import re
if __name__ == '__main__':
    str:str = "Rot ator"
    print(isPalindrome(str))


