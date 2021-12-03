#dx = [-1, 1, 0, 0]
#dy = [0, 0, -1, 1]

# 0 0 0   [0, 0], [1, 0], [2, 0]
# 0 1 0   [0, 1], [1, 1], [2, 1]
# 0 0 0   [0, 2], [1, 2], [2, 2]

#bx = [1, -1, -1, 1]
#by = [1, -1, 1, -1]

#x, y = [1, 1]

#for i in range(4):
#    a = x + dx[i]
#    b = y + dy[i]
#    c = x + bx[i]
#    d = y + by[i]
#    print(a, ", ", b, " | ", c, ", " ,d)

### 백준 7576번 토마토

from collections import deque

def bfs(graph, m, n, answer):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while len(queue) != 0:
        answer += 1

        for _ in range(len(queue)):
            x, y = queue.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if (0 <= nx < n) and (0 <= ny < m) and (graph[nx][ny] == 0):
                    queue.append([nx, ny])
                    graph[nx][ny] = graph[x][y] + 1

    for check in graph:
        if 0 in check:
            return -1
    
    return answer

m, n = map(int, input().split())
graph , queue= [], deque([])

for i in range(n):
    graph.append(list(map(int, input().split())))

    for j in range(m):
        if graph[i][j] == 1:
            queue.append([i, j])

print(bfs(graph, m, n, -1))


# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 1
# 5, 3