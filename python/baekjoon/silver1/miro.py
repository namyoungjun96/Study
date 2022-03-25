# 백준 2178번 미로탐색
# 못풀었다. (다른분거 참고)
# BFS는 원래 최단거리를 탐색하게 돼있다... 알아두자. 

import sys
from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

n, m = map(int, sys.stdin.readline().split())
graph = []
visited = [[False]*m for i in range(n)]

for i in range(n):
    temp = sys.stdin.readline().rstrip()
    temp = list(temp)
    graph.append(temp)
    
def bfs(graph):
    queue = deque()
    queue.append((0, 0))
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx >= n or nx < 0 or ny >= m or ny < 0:
                continue

            if graph[nx][ny] == "1" and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
                
    print(visited[x][y])

bfs(graph)