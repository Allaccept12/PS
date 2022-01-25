



def rainHight(src):
    #높이를 입력받아 비 온 후 얼마나 많은 물이 쌓일 수 있는지 계산하라

    #양쪽 시작위치
    left = 0
    right = len(src)-1
    #양쪽 최대 높이
    left_h = src[left]
    right_h = src[right]
    #물
    water = 0
    #처음부터 끝까지
    while left < right:
        #지금 현재 위치가 전에보다 높나
        #0,1,0,2,1,0,1,3,2,1,2,1
        left_h = max(src[left],left_h)
        right_h = max(src[right],right_h)

        if left_h < right_h:
            water += left_h - src[left]
            left += 1
        else:
            water += right_h - src[right]
            right -= 1
        print(water)








if __name__ == '__main__':
    print(rainHight([0,1,0,2,1,0,1,3,2,1,2,1]))