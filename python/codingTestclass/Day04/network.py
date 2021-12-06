# 프로그래머스 DFS, BFS 3단계 네트워크
# BFS 는 깊이 우선이 아닌 너비 우선. 다시 주의깊게 풀어보자..!!!

from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False] * n

    answer = bfs(computers, visited, 0, 1)
    print("first answer : ", answer)
    return answer

def bfs(graph, visited, index, answer):
    visited[index] = True
    queue = deque([])
    queue.append(graph[index])
    
    while queue:
        check = queue.popleft()
        
        for i in range(len(check)):
            if check[i] == 1 and visited[i] == False and i != index:
                visited[i] = True
                index = i
                print("first : ", answer)
                break
            elif check[i] == 1 and visited[i] == False and i == index:
                answer += 1
                visited[i] = True
                index = i
                print("second : ", answer)
            elif visited[i] == False:
                index = i
                print("third : ", answer)
                
        if False in visited:
            queue.append(graph[index])
                
    return answer

n = 3
n2 = 4
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
computers2 = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
computers3 = [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 0], [1, 1, 0, 1]]

solution(n, computers)
print('========================')
solution(n, computers2)
print('========================')
solution(n2, computers3)

# [[1, 1, 0], [1, 1, 1], [0, 1, 1]], 3