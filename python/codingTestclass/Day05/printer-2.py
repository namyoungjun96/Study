from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque([])

    for i in range(len(priorities)):
        queue.append(i)
    first = priorities[0]

    while queue:
        for i in range(len(priorities)):
            if first < priorities[i]:
                first = priorities[i]
                temp = queue.popleft()
                queue.append(temp)

        answer += 1
        temp = queue.popleft()
        if location == temp:
            break

    print(answer)
    return answer

priorities,	location = [2, 1, 3, 2], 2
priorities2, location2 = [1, 1, 9, 1, 1, 1], 0

solution(priorities, location)