
def threeElemSum(src):
    if src == [[0,0,0]]:
        return [[0, 0, 0]]
    src.sort()
    first = 0  # 시작 수
    last = len(src) - 1  # 끝 수
    result = []  # 결과 리스트
    index = 0  # 순차적인 인덱스


    num_index = 0
    while first < len(src):
        while True:
            num_index += 1
            if src[first]+src[last]+src[last-num_index] == 0:
                result.append([src[first],src[last],src[last-num_index]])
            if num_index - last == 1:
                break
            if first + 1 == last - num_index:
                last -= 1
                num_index = 0

            if first == 3:
                break
        if first == 3:
            break
        index += 1
        first = index
        last = len(src) - 1
        num_index = 0
# 021, 132, 243, 354
    sots = []

    for sot in result:
        sot.sort()
        if not sot in sots:
            sots.append(sot)

    return sots


if __name__ == '__main__':
    print(threeElemSum([-1,0,1,0]))