import collections
import heapq
import sys


n = int(input())
temp = 0
arr = []
for i in range(0,n):
    temp = int(sys.stdin.readline())
    if temp != 0:
        heapq.heappush(arr,temp)
    else:
        if len(arr) != 0:
            arr = heapq.nlargest(len(arr),arr)
            print(arr.pop(0))
        else:
            print(0)
    print("i  n",i , n)







