import bisect

#bisect.bisect_left
#bisect.bisect_right

#[-1,1,2,2,2,3] 2 -> 많다면 같거나큰값의 시작인덱스값
#bisect_left -> 2

#[-1,1,3,3,4] 2 찾는값보다 같거나큰값의 시작인덱스값
#bisect_left -> 2

#[-1,-1,-2,-2,-2,-3] 2 타겟보다 다작다면 배열의 길이를 반환
#bisect_left -> 6

#필수 조건 if idx < len(배열)  and 배열[idx] == target:
    # return idx
import heapq

def binary_search_builtin(nums, target):
    idx = bisect.bisect_left(nums, target)
    if idx < len(nums) and nums[idx] == target:
        return idx
    else:
        return -1