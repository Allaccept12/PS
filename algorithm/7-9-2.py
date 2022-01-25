








def threeSum(src):
    result = []
    src.sort()

    for i in range(len(src)-2):
        if i>0 and src[i] == src[i-1]:
            continue
        l = i+1
        r = len(src)-1
        while l<r:
            if src[i] + src[l] + src[r] < 0:
                l += 1
            elif src[i] + src[l] + src[r] > 0:
                r -= 1
            else:
                result.append([src[i], src[l], src[r]])

                l += 1
                r -= 1

    return result




if __name__ == '__main__':
    print(threeSum([-2,0,0,2,2]))