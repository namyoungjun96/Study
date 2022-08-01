import sys

n, m = map(int, sys.stdin.readline().split())
graph = []
answer = 0

for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    answer = max(answer, min(temp))

print(answer)

# 3 3
# 3 1 2
# 4 1 4
# 2 2 2

# 2 4
# 7 3 1 8
# 3 3 3 4