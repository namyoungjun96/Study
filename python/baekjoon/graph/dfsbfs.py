import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())
graph = [[0] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    node, node2 = (list(map(int, input().split())))
    graph[node][node2] = graph[node2][node] = 1
                
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")
    
    for i in range(len(graph[v])):
        if not visited[i] and graph[v][i]:
            dfs(graph, i, visited)
                
def bfs(graph, v, visited):
    visited[v] = True
    queue = deque([graph[v]])
    print(v, end=" ")
    
    while queue:
        temp = queue.popleft()
        
        for i in range(len(temp)):
            if temp[i] and not visited[i]:
                queue.append(graph[i])
                visited[i] = True
                print(i, end=" ")

dfs(graph, v, visited)
visited = [False] * (n+1)
print()
bfs(graph, v, visited)