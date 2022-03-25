# 백준 2667번 단지번호붙이기
# 20분

import sys
from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

n = int(sys.stdin.readline())
graph = list()
for i in range(n):
    temp = sys.stdin.readline().rstrip()
    temp = list(temp)
    graph.append(temp)
queue = deque()
answer = list()

def bfs(graph, startx, starty):
    graph[startx][starty] = 0
    queue.append((startx, starty))
    danzi = 1
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx >= n or nx < 0 or ny >= n or ny < 0:
                continue

            if graph[nx][ny] == "1":
                graph[nx][ny] = "0"
                queue.append((nx, ny))
                danzi += 1
                
    return danzi
    
for i in range(len(graph)):
    for j in range(len(graph)):
        if graph[i][j] == "1":
            answer.append(bfs(graph, i, j))
    
answer.sort()

print(len(answer))        
for i in range(len(answer)):
    print(answer[i])