


"""
    상위 k번 이상 등장하는 요소를 추출하라
"""
import collections

if __name__=="__main__":
    nums = [1,1,1,2,2,3]
    k = 2

    count = 1
    result = []
    dic = {}
    for n in nums:
        dic[n] = 0
    print(dic.items())
    for s in nums:
        if s in dic:
            count +=1





    #
    # counter = collections.Counter(nums)
    # result = []
    # keys = counter.keys()
    # for i in range(1,len(counter.keys())+1):
    #     pass

