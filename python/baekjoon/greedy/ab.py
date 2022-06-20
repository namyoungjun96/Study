import sys
from collections import deque

def bfs(num, target):    
    res = []
    q = deque([(0, num)])
    
    while q:
        count, num = q.popleft()
        count += 1
        
        if num == target:   # 2랑 162가 같아질 경우
            res.append(count)
        
        elif num > target:  # 2보다 커질경우
            continue
        
        else:               # 2한테 *2를 하거나 오른쪽에 1을 붙일경우
            tmp = num
            tmp = num * 2 
            q.append((count, tmp)) 
            tmp2 = str(num)
            tmp2 += "1"
            q.append((count, int(tmp2)))
    return res

a, b = map(int, sys.stdin.readline().split())

res = bfs(a, b)
print(res)

if res:
    print(min(res))
else:
    print(-1)