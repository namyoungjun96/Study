# 프로그래머스 스택/큐 2단계 다리를 지나는 트럭

from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights.reverse()
    timeList = deque()
    currentWeight = 0

    while timeList:
        if truck_weights[len(truck_weights)-1] + currentWeight < weight:
            timeList.append(truck_weights.pop())
        
        if timeList[0]

    return answer

bridge_length, weight, truck_weights = 2, 10, [7,4,5,6]	
#100	100	[10]
#100	100	[10,10,10,10,10,10,10,10,10,10]

solution(bridge_length, weight, truck_weights)