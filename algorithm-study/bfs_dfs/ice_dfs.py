

def iceSol(row,col,ices):
    visited = [0] * col
    iceCream = 0

    def dfs(x,y):
        if x <= -1 or x >= len(row) or y <= -1 or y >= len(col):
            return False
        if ices[x][y] == 0:
            ices[x][y] = 1
            dfs(x-1, y)
            dfs(x+1, y)
            dfs(x,y+1)
            dfs(x,y-1)
            return True
        return False

    for i in range(row):
        for j in range(col):
            if dfs(i,j) == True:
                iceCream += 1






iceSol(4,5,[
    [0,0,1,1,0],
    [0,0,0,1,1],
    [1,1,1,1,1],
    [0,0,0,0,0],
])