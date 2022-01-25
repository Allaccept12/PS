





"""
모든 명함을 수납 할 수 있는 가장 작은 지갑을 만들때 지갑의 크기 리턴
w = 가로
h =  세로
"""


if __name__ == '__main__':
    sizes = [[14,4],[19,6],[6,16],[18,7],[7,11]]
    maxLine = 0
    minLine = min(sizes[0])
    for i in range(0,len(sizes)):

        maxLine = max(max(sizes[i]),maxLine)
        minLine = max(min(sizes[i]), minLine)
        print(maxLine, minLine)

    return maxLine*minLine


