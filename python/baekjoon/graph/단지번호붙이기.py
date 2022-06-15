import sys
from collections import deque

n = int(input())
graph = []
visited = [[0] * (n) for _ in range(n)]
queue = []
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
answer = []

for i in range(n):
    temp = list(map(int, input()))
    graph.append(temp)
    
for i in range(n):
    for j in range(n):
        if graph[i][j]:
            queue.append((i, j))
    
def bfs(graph, visited, queue):
    danzi = []
    for x, y in queue:
        if visited[x][y] > 0:
            continue
        else:
            temp = deque([(x, y)])
            count = 0
            visited[x][y] = 1
            
            while temp:
                x, y = temp.popleft()
                count += 1
                
                for i in range(4):
                    px = x + dx[i]
                    py = y + dy[i]
                    
                    if (px >= 0 and py >= 0 and px < n and py < n and graph[px][py] and not visited[px][py]):
                        temp.append((px, py))
                        visited[px][py] = 1
            
            danzi.append(count)
    return danzi
    
answer = bfs(graph, visited, queue)
answer.sort()

print(len(answer))
for i in range(len(answer)):
    print(answer[i])