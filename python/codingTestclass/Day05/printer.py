# 프로그래머스 스택/큐 2단계 프린터

from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque([])

    for i in range(len(priorities)):
        queue.append(priorities[i])
        
    while queue:
        for i in range(len(queue)-1):
            if queue[0] < queue[i]:
                queueValue = queue.popleft()
                queue.append(queueValue)
                if location > 0 :
                    location -= 1
                    break
                else:
                    location = len(queue)-1
                
        if queue[0] == max(queue):
            answer += 1
            if location == 0:
                break
            queue.popleft()
            location -= 1
            
    return answer

priorities,	location = [2, 1, 3, 2], 2
priorities2, location2 = [1, 1, 9, 1, 1, 1], 0

solution(priorities, location)
print("======================")
solution(priorities2, location2)