import collections


def bfs_sol():
    graph = [
        [],
        [2, 3, 8],
        [1, 7],
        [4, 5],
        [3, 5],
        [3, 4],
        [7],
        [6, 8],
        [1, 7]
    ]
    visited = [False] * 9
    def bfs(graph, start, visited):
        q = collections.deque([start])
        visited[start] = True

        while q:
            cur = q.popleft()
            print(cur)
            for idx in graph[cur]:
                if not visited[idx]:
                    bfs(graph, idx, visited)


    bfs(graph, 1, visited)

bfs_sol()