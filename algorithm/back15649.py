




"""
n = 1~ n
m = 수열의 길이
"""
n = 9
m = 9
visited = [False] * (n+1)
res = []
def dfs(v):
    if m == v:
        print(' '.join(map(str, res)))
        return
    for i in range(1, n + 1):
        if visited[i] == False:
            visited[i] = True
            res.append(i)
            dfs(v + 1)
            visited[i] = False
            res.pop()
dfs(0)
