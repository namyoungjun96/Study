from collections import deque

def bfs(graph, start, visited):
    queue=deque([start])
    visited[start]=True

    while queue:
        v = queue.popleft()
        print(v, end=" ")                           ## 문제에서 처리 해야 할 사항
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited=[False]*len(graph)

bfs(graph, 1, visited)