# 백준 1260번 bfs와 dfs

from collections import deque

def dfs(graph, start, visited):
    visited.append(start)
    print(start, end=' ')

    for i in range(len(graph[start])):
        if graph[start][i] == 1 and i not in visited:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    visited = [start]
    queue = deque()
    queue.append(start)

    while queue:
        check = queue.popleft()
        print(check, end=' ')

        for i in range(len(graph[start])):
            if graph[check][i] == 1 and i not in visited:
                visited.append(i)
                queue.append(i)

inputList = list(map(int, input().split()))
N, M, V = inputList[0], inputList[1], inputList[2]

graph = [[0] * (N+1) for _ in range(N+1)]

for i in range(M):
    node, node2 = (list(map(int, input().split())))
    graph[node][node2] = graph[node2][node] = 1

print(graph)

visited=[]
dfs(graph, V, visited)

print()

visited=[]
bfs(graph, V, visited)

'''
1 2
1 3
1 4
2 4
3 4
'''