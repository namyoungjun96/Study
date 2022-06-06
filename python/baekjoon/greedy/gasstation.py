import sys

n = int(input())
position = list(map(int, sys.stdin.readline().split()))
position.reverse()
country = list(map(int, sys.stdin.readline().split()))
country.pop()
temp = position.pop()
fuel = 0
answer = 0

for i in range(n-1):
    if country[i] == min(country):
        answer += (temp + sum(position)) * country[i]
        break
    else:
        answer += (temp - fuel) * country[i]
        fuel += (temp - fuel)

    if fuel >= temp:
        fuel -= temp
        
        if position:
            temp = position.pop()

print(answer)

# 5
# 2 3 1 1
# 5 2 4 1 1
# 19