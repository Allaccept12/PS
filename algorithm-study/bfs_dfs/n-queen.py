





def n_queen(n):
    visited = [-1] * n
    answers = []


    def is_ok(q_row):
        for row in range(q_row):
            if visited[q_row] == visited[row] or q_row - row == abs(visited[q_row] - visited[row]):
                return False
        return True


    def dfs(row):
        if row >= n:
            grid = [['.'] * n for _ in range(n)]
            for i,num in enumerate(visited):
                grid[i][num] = 'Q'
            result = []
            for row in grid:
                print(row)
                result.append(''.join(row))
            answers.append(result)
            return

        for col in range(n):
            visited[row] = col
            if is_ok(row):
                dfs(row+1)


    dfs(0)
    return answers








print(n_queen(4))







