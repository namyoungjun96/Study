# 백준 2178번 미로 탐색

inputList = list(map(int, input().split()))
N, M = inputList[0], inputList[1]

graph = []
start = [0, 0]
visited = [[False] * (M) for _ in range(N)]
answer = 1

for i in range(N):
    temp = list(map(int, input()))
    graph.append(temp)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(graph, start, visited):
    global answer
    x=start[0]
    y=start[1]
    visited[x][y] = True

    if x == len(graph)-1 and y == len(graph[x])-1:
        print(answer)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if (0 <= nx < len(graph)) and (0 <= ny < len(graph[nx])) and graph[nx][ny] == 1 and visited[nx][ny] == False:
            answer += 1
            dfs(graph, [nx, ny], visited)

dfs(graph, start, visited)