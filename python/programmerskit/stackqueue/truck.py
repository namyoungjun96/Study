# 프로그래머스 스택/큐 2단계 다리를 지나는 트럭
# DAY 06 문제풀이

from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights.reverse()
    timeList = deque()
    timeList.append(1)
    currentWeight = deque()
    currentWeight.append(truck_weights.pop())
    count = len(truck_weights)-1
    time = 1

    while timeList:
        if timeList[0] == bridge_length:
            timeList.popleft()
            currentWeight.popleft()
        
        if count >= 0 and sum(currentWeight) + truck_weights[count] <= weight and len(currentWeight) <= bridge_length:
            currentWeight.append(truck_weights.pop())
            timeList.append(0)
            count -= 1
        
        for i in range(len(timeList)):
            timeList[i] += 1
        time += 1
            
    answer = time
    print(answer)
    return answer

# bridge_length, weight, truck_weights
test = [
    [2, 10, [7,4,5,6]],
    [100, 100, [10]],
    [100, 100, [10,10,10,10,10,10,10,10,10,10]]]

for i in range(3):
    solution(test[i][0], test[i][1], test[i][2])