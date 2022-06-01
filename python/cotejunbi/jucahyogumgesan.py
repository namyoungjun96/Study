# 주차 요금 계산

from collections import defaultdict
import math

def solution(fees, records):
    answer = []
    client = defaultdict(list)
    
    while records:
        temp = (records.pop(0)).split()
            
        if temp[1] not in client:
            client[temp[1]].append([temp[0], temp[2]])
        else:
            client[temp[1]].append([temp[0], temp[2]])
            
    for key in client.keys():
        answer.append(key)
        value = 0
        while client[key]:
            temp = client[key].pop(0)
            time = temp[0].split(":")
            minute = int(time[0]) * 60 + int(time[1])
            if temp[1] == 'IN':
                if client[key]:
                    value -= minute
                else:
                    value += ( 1439 - minute )
            else:
                value += minute
        if value - fees[0] > 0:
            client[key] = fees[1] + math.ceil((value - fees[0]) / fees[2]) * fees[3]
        else:
            client[key] = fees[1]
    
    answer.sort()
    for i in range(len(answer)):
        answer[i] = int(client[answer[i]])
        
    return answer