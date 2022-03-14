# 다음에 다시 풀어보자.. 문제에 말한 의도가 이해가 안된다.

n = int(input())
#n = 3
house = [list(map(int, input().split())) for _ in range(n)]
#house = [[26, 40, 83], [49, 60, 57], [13, 89, 99]]
#house = [[1, 100, 100], [100, 1, 100], [100, 100, 1]]
answer = 0
visited = -1

for i in range(len(house)):
    minimum = 1001
    check = 0
    for j in range(len(house[0])):
        if j != visited and minimum > house[i][j]:
            check = j
            minimum = house[i][j]
    visited = check
    answer += minimum
    
print(answer)