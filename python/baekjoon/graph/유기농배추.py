import sys
from collections import deque

t = int(input())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
answer = []

for i in range(t):
    n, m, k = map(int, input().split())
    graph = [[0] * (n) for _ in range(m)]
    visited = [[False] * (n) for _ in range(m)]
    cabbage = []
    count = 0
    
    for j in range(k):
        x, y = map(int, input().split())
        
        graph[y][x] = 1
        cabbage.append([x, y])
        
    for pos in cabbage:
        if not visited[pos[1]][pos[0]]:
            queue=deque([(pos[0], pos[1])])
            while queue:
                x, y = queue.popleft()
                for i in range(4):
                    px = x + dx[i]
                    py = y + dy[i]
                    
                    if (px >= 0 and py >= 0 and px < n and py < m and graph[py][px] and not visited[py][px]):
                        queue.append((px, py))
                        visited[py][px] = True
            count += 1
    
    answer.append(count)

for i in answer:
    print(i)