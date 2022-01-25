








def solution(n, danji):
    visited = [[0] * n for _ in range(n)]
    cnt = 0
    result = []
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]

    def dfs(x,y):
        nonlocal cnt
        cnt += 1
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0 <= nx <n and 0 <= ny < n:
                if danji[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    dfs(nx,ny)
    for i in range(n):
        for j in range(n):
            if danji[i][j] == 1 and visited[i][j] == 0:
                visited[i][j] = 1
                cnt = 1
                dfs(i,j)
                result.append(cnt)

    result.sort()
    print(len(result))
    for i in result:
        print(i)




solution(7,[
[0,1,1,0,1,0,0],
[0,1,1,0,1,0,1],
[1,1,1,0,1,0,1],
[0,0,0,0,1,1,1],
[0,1,0,0,0,0,0],
[0,1,1,1,1,1,0],
[0,1,1,1,0,0,0],
])