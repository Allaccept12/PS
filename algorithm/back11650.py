







"""
def quicksort(lst, start, end):
    def partition(part, ps, pe):
        pivot = part[pe]
        i = ps - 1
        for j in range(ps, pe):
            if part[j] <= pivot:
                i += 1
                part[i], part[j] = part[j], part[i]

        part[i + 1], part[pe] = part[pe], part[i + 1]
        return i + 1

    if start >= end:
        return None

    p = partition(lst, start, end)
    quicksort(lst, start, p - 1)
    quicksort(lst, p + 1, end)
    return lst
"""




import sys
input = sys.stdin.readline
n=int(input())
#2차원 배열 매핑
# for i in range(n):
#     [a, b] = list(map(int, input().split()))
#     arr.append([a,b])
arr=[list(map(int,input().split())) for i in range(n)]
arr.sort(key = lambda x: (x[0],x[1]))
#arr.reverse() 2
for j in arr:
    print("%d %d"%(j[0],j[1]))

