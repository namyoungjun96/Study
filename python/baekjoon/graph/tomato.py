import sys
from collections import deque

def bfs(graph, temp, m, n):
    answer = -1
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    while temp:
        queue = deque(temp)
        temp = []
        
        while queue:
            y, x = queue.popleft()
            
            for i in range(4):
                px = x + dx[i]
                py = y + dy[i]
                
                if (px >= 0 and py >= 0 and px < m and py < n and graph[py][px] == 0):
                    temp.append((py, px))
                    graph[py][px] = 1
        answer += 1
        
    for i in graph:
        if 0 in i:
            answer = -1
    
    return answer

m, n = map(int, sys.stdin.readline().split())
graph = []
temp = []
cnt = 0

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))
    
    if 1 in graph[i]:
        for j in range(len(graph[i])):
            if graph[i][j] == 1:
                temp.append((i, j))
            elif graph[i][j] == 0:
                cnt += 1

if cnt:
    answer = bfs(graph, temp, m, n)
    print(answer)
elif not temp:
    print(-1)
else:
    print(0)