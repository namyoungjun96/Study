n = int(input())
bulk = list()
answer = [1] * n

for i in range(n):
    x, y = map(int, input().split())
    bulk.append([x, y])

for i in range(n):
    for j in range(n):
        if bulk[i][0] < bulk[j][0] and bulk[i][1] < bulk[j][1]:
            answer[i] += 1
            
for i in range(n):
    print(answer[i], end=" ")