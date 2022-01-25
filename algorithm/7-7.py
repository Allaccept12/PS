import collections


def twoSum(nums,target):
    # nums_map = {}
    #
    # for i,n in enumerate(nums):
    #     if target-n in nums_map:
    #         return [nums_map[target-n],i]
    #     nums_map[n] = i
    temp = collections.deque([1,2,3,4])
    len(temp)
    print(len(temp))

    if not temp:
        print('sds')
    else:
        print('ss')






#twosum 덧셈하여 타겟을 만들수있는 배열의 두 숫자 인덱스를 리턴
if __name__ == '__main__':
    print(twoSum([2,8,11,12,20,9,4],20))

