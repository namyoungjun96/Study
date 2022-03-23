# 백준 1012번 유기농 배추
# 2시간은 걸린듯
# 파이썬은 2차원 배열을 선언하면서 시간이 오래걸린다. (2차원 배열의 객체크기가 클경우)
# 객체 생성의 횟수가 적은쪽이 유리하다.
# 시간 제한이 짧다면 visited를 선언하지않고 푸는것을 추천..
# 그리고 dx, dy 더하고 빼는건 좌표 문제에서 필수적으로 기억할 것

import sys
from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(graph, startx, starty):
    queue = deque()
    queue.append((startx, starty))
    graph[startx][starty] = 0
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx >= n or nx < 0 or ny >= m or ny < 0:
                continue
            
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                
    return

testcase = int(sys.stdin.readline())
answer = [0] * testcase

for i in range(testcase):
    n, m, k = map(int, sys.stdin.readline().split())
    graph = [[0]*m for i in range(n)]
    stack = [0] * (k*2)
    count = 0
    
    for j in range(k):
        posx, posy = map(int, sys.stdin.readline().split())
        graph[posx][posy] = 1
        stack[count] = posx
        stack[count+1] = posy
        count += 2
        
    for j in range(0, len(stack), 2):
        if graph[stack[j]][stack[j+1]] == 1:
            bfs(graph, stack[j], stack[j+1])
            answer[i] += 1

for i in range(testcase):
    print(answer[i])