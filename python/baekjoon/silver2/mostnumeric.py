# 백준 11053번 가장 긴 증가하는 부분 수열

import sys

n = sys.stdin.readline().split()
numeric = list(map(int, sys.stdin.readline().split()))
count = [1] * len(numeric)
for i in range(1, len(numeric)):
    for j in range(i):
        if numeric[i] > numeric[j]:
            count[i] = max(count[i], count[j]+1)
            
print(count)

# 6
# 1 2 8 2 4 8

# Ans: 4 (1, 2, 4, 8)
# Out: 3