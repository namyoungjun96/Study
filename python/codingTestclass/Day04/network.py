# 프로그래머스 DFS 3단계 네트워크

def solution(n, computers):
    answer = 0

    visited = [False] * n

    print(computers)

    answer = dfs(computers, visited, 0, answer)
    print(answer)
    return answer

def dfs(graph, visited, start, answer):
    visited[start]=True

    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j] == 1 and visited[i] == False:
                dfs(graph, visited, j, answer+1)

n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

solution(n, computers)