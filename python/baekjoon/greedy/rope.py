import sys

n = int(input())
rope = []
answer = 0

for i in range(n):
    rope.append(int(sys.stdin.readline()))
    
rope.sort()

for i in range(1, n+1):
    temp = rope.pop()
    answer = max(answer, temp*i)

print(answer)