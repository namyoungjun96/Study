import sys

t = int(input())
n = list(map(int, sys.stdin.readline().split()))
# answer = []

for i in range(t):
    line = []
    count = 0
    
    while n[i] > 0:
        if n[i] % 2 == 1:
            line.append(count)
            
        n[i] //= 2
        count += 1
    
    print(' '.join(map(str, line)))

# for i in range(len(answer)):
#     for j in range(len(answer[i])):
#         print(answer[i][j], end=" ")
#     print()