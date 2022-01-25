




def longPalindrome(src):
    #dddd
    def ispalinderome(l,r):
        while l > 0 and r < len(src) and src[l] == src[r]:
            print(l, r)
            l -= 1
            r += 1
        return src[l+1 : r]

    if len(src) < 2 or src == src[::-1]:
        return src

    result = ''
    for i in range(len(src) - 1):
        result = max(result, ispalinderome(i,i),ispalinderome(i,i+1),
                     key=len)
    print(result)

if __name__ == '__main__':
    longPalindrome('dddc')
