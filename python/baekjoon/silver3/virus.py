# 백준 2606번 바이러스

import sys

number = int(sys.stdin.readline())
cell = int(sys.stdin.readline())
graph = [[0 for i in range(number+1)] for j in range(number+1)] 
visited = [False] * (number + 1)

def dfs(graph, start, visited):
    visited[start] = True
    
    for i in range(len(graph)):
        if graph[start][i] == 1 and visited[i] == False:
            dfs(graph, i, visited)
    
    return 0

for i in range(cell):
    connect1, connect2 = map(int, sys.stdin.readline().split())
    graph[connect1][connect2] = 1
    graph[connect2][connect1] = 1
    
dfs(graph, 1, visited)

print(visited.count(True)-1)