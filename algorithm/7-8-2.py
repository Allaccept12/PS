







#높이가 주어지고 빗물이 얼마나 쌓일수있는지 계산
#양쪽으로 투포인터를 잡고 건물 높이가 높은쪽이 움직이고 낮은쪽이 움직이는 구조
#그래서 가장 높은 건물에서 포인터 두개가 만나면 return
def water(src):
    left = 0
    right = len(src)-1
    #현재
    l_h = src[left]
    r_h = src[right]
    waters = 0
    while left <= right:
        l_h = max(src[left],l_h)
        r_h = max(src[right],r_h)

        if l_h < src[right]:
            waters += l_h - src[left]
            left += 1
        else:
            waters +=  r_h -src[right]
            right -= 1

    return waters


if __name__ == '__main__':
    print(water([0,1,0,2,1,0,1,3,2,1,2,1]))