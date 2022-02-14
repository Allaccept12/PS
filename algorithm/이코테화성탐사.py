import sys



INF = int(1e9)
input = sys.stdin.readline

dx = [0,1,0,-1]
dy = [1,0,-1,0]

t = int(input())

for _ in range(t):
    n = int(input())
    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))
    dis = [[INF] * n for _ in range(n)]
    