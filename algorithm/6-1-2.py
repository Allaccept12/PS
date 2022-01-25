


def pallindrome(src):
    src = ''.join(e for e in src if e.isalnum()).lower()
    print(src)
    return src == src[::-1]


if __name__ == "__main__":
    print(pallindrome("Race A Car"))
