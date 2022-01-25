"""
1, Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
1이 뭉쳐있는 섬의 개수를 세어라
"""
def solution (grid):
    gx = [0,0,1,-1]
    gy = [1,-1,0,0]
    row, col= len(grid), len(grid[0])
    island = 0
    for r in range(row):
        for c in range(row):
            if grid[r][c] != '1':
                continue
            island += 1
            stack = [(r,c)]

            while stack:
                x,y = stack.pop()
                grid[x][y] = '0'
                for i in range(4):
                    nx = x + gx[i]
                    ny = y + gy[i]
                    if nx < 0 or nx >= row or ny < 0 or ny >= col or grid[nx][ny] != '1':
                        continue
                    stack = [(nx,ny)]

    print(island)
    return island



solution([
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
])