import sys

n = int(input())
position = list(map(int, sys.stdin.readline().split()))
country = list(map(int, sys.stdin.readline().split()))
country.pop()
fuel = country[0]
answer = 0

for i in range(n-1):
    if country[i] < fuel:
        fuel = country[i]
    answer += fuel * position[i]

print(answer)

# 5
# 2 3 1 1
# 5 2 4 1 1
# 19