import sys
from collections import deque

def bfs(num, target):    
    res = []
    q = deque([(0, num)])
    
    while q:
        count, num = q.popleft()
        
        if num == target:
            res.append(count)
            break
        
        elif num < 0:
            continue
        
        else:
            count += 1
            tmp = num
            tmp += 1 
            q.append((count, tmp)) 
            tmp2 = num
            tmp2 *= 2
            q.append((count, tmp2))
            
            if num > 0:
                tmp3 = num
                tmp3 -= 1
                q.append((count, tmp3))
    return res

n, k = map(int, sys.stdin.readline().split())

res = bfs(n, k)

if res:
    print(res[0])
else:
    print(0)