import collections


def removeDuplicate(s):
    # temp = []
    # count = collections.Counter(src)
    # print(count)
    """"" cbacdcbc
     1, 1개인 아이의 위치를 고정한다
     2, a = 2, d = 4  -> 인덱스 위치 고정
     3, 사전순을 찾는다
     4, 그 중에서 사준순 으로 가장 빠른 알파벳(가파벳)을 기준으로 왼쪽 오른쪽으로 나누고 
     5, 가파벳 다음 것을 찾는다 how? 
        5-1 가파벳 기준으로 오른쪽에 가파벳 다음 알파벳이 하나이상 있으면 왼쪽에 있는 가파벳 다음것을 삭제
        5-2 삭제가 됬다면 
     6,   
     7, 
    """""

    res = []  # empty stack    cbacdcbc
    for i in range(len(s)):
        if s[i] in res: continue
        if res:
            print(s[i],s[i]<res[-1] ,res[-1])
        while res and s[i] < res[-1] and res[-1] in s[i + 1:]:
            res.pop()
            print(res)
        res.append(s[i])
        print(res)

    return "".join(res)


    # return ''.join(sorted(temp))
    # result = [arr[:]]
    # c = [0] * len(arr)
    # i = 0
    # while i < len(arr):
    #     if c[i] < i:
    #
    #         if i % 2 == 0:
    #             arr[0], arr[i] = arr[i], arr[0]
    #         else:
    #             arr[c[i]], arr[i] = arr[i], arr[c[i]]
    #         result.append(arr[:])
    #
    #         c[i] += 1
    #         i = 0
    #     else:
    #         c[i] = 0
    #         i += 1
    # return result




if __name__ == '__main__':
    print(removeDuplicate("cbacdcbc"))