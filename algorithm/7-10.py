




def arrayPartition(src):
    # n개의 페어를 이용한 min(a,b)의 합으로 만들수있는 가장 큰수를 출력하라
    # 두개씩 솔팅하면 0 2 4.. 값이 가장 작은수들을 뽑아서 리스트로 뽑아서 가장 큰수 더하기

    #풀이 2
    list = (sorted(src)[::2])
    return sum(list)

    #풀이 1
    # src.sort()
    # pair = []
    # result = 0

    # for i in range(0,len(src)-1):
    #     if i % 2 == 0:
    #         pair.append([src[i],src[i+1]])
    #     else:
    #         continue
    # for i in range(0, len(pair)):
    #     result += min(pair[i])
    #
    # return result


if __name__ == '__main__':
    #pair -> 01 12 23 34
    print(arrayPartition([1,4,3,2,0,2,3,1]))