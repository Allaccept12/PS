import heapq
import sys

"""
10,20,40,50,30
10+20 + 30+30 + 60+40 + 100+50 = 340
30 + 60 + 100 + 150

10,20,40
30 + 70 = 100

10+20
"""


n = int(sys.stdin.readline())
heap = list(int(sys.stdin.readline().rstrip()) for i in range(n))
heapq.heapify(heap)

result = 0
while len(heap) != 1:
    fir = heapq.heappop(heap)
    sec = heapq.heappop(heap)
    result += fir + sec
    heapq.heappush(heap,fir + sec)

print(result)
