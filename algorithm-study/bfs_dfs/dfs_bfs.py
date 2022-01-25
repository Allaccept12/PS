"""


"""




def dfs_sol():
    graph =[
        [],
        [2,3,8],
        [1,7],
        [4,5],
        [3,5],
        [3,4],
        [7],
        [6,8],
        [1,7]
    ]
    visited = [False] * 9
    def dfs(graph,cur,visited):
        visited[cur] = True
        print(cur)
        for idx in graph[cur]:
            if not visited[idx]:
                dfs(graph,idx,visited)

    dfs(graph,1,visited)

dfs_sol()