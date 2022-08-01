import sys

n, m, k = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
num.sort(reverse=True)
answer = 0

first = num[0]
second = num[1]

# for i in range(1, m+1):
#     if i%k == 0:
#         answer += second
#     else:
#         answer += first

count = int(m / (k + 1)) * k

answer += (count * first) + ((m - count) * second)
    
print(answer)