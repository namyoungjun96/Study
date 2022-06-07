import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = []
visited = [[0] * (m) for _ in range(n)]
for i in range(n):
    temp = list(map(int, input()))
    graph.append(temp)
    # temp = list(map(int, sys.stdin.readline().split()))
    # graph.append(temp)
    
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
    
def bfs(graph, startx, starty, visited):
    visited[starty][startx] = 1
    queue = deque([(starty, startx)])
    # print(temp[0], temp[1])
    
    while queue:
        temp = queue.popleft()
        
        for i in range(4):
            y = temp[0] + dy[i]
            x = temp[1] + dx[i]
            
            if (x >= 0 and y >= 0 and x < m and y < n and graph[y][x] and not visited[y][x]):
                queue.append((y, x))
                visited[y][x] = visited[y-dy[i]][x-dx[i]] + 1
    
bfs(graph, 0, 0, visited)
print(visited[n-1][m-1])

# def dxdy(graph, startx, starty, visited):
#     visited[startx][starty] = 1
#     queue = deque([(startx, starty)])
#     temp = queue.popleft()
    
#     for i in range(4):
#         print(temp[0] + dx[i], temp[1] + dy[i])
        
# dxdy(graph, 0, 0, visited)