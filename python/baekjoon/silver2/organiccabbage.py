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

def bfs(graph, starty, startx):
    queue = deque()
    queue.append((starty, startx))
    graph[starty][startx] = 0
    
    while queue:
        starty, startx = queue.popleft()
        
        for i in range(4):
            ny = starty + dy[i]
            nx = startx + dx[i]
            
            if ny >= n or ny < 0 or nx >= m or nx < 0:
                continue
            
            if graph[ny][nx] == 1:
                graph[ny][nx] = 0
                queue.append((ny, nx))
                
    return

testcase = int(sys.stdin.readline())
answer = [0] * testcase

for i in range(testcase):
    m, n, k = map(int, sys.stdin.readline().split())
    x, y = 0, 0
    graph = [[0 for i in range(m)] for j in range(n)]
    stack = [0] * (k*2)
    count = 0
    
    for j in range(k):
        posx, posy = map(int, sys.stdin.readline().split())
        graph[posy][posx] = 1
        stack[count] = posy
        stack[count+1] = posx
        count += 2
        
    for j in range(0, len(stack), 2):
        if graph[stack[j]][stack[j+1]] == 1:
            bfs(graph, stack[j], stack[j+1])
            answer[i] += 1

for i in range(testcase):
    print(answer[i])