import sys

n = int(input())
connect = int(input())
graph = [[0] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1)

for i in range(connect):
    node, node2 = (list(map(int, input().split())))
    graph[node][node2] = graph[node2][node] = 1
    
def dfs(graph, v, visited):
    visited[v] = True
    
    for i in range(n+1):
        if graph[v][i] and not visited[i]:
            dfs(graph, i, visited)
    
dfs(graph, 1, visited)
print(sum(visited)-1)