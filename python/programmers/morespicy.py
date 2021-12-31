# 프로그래머스 우선순위 큐 2단계 더 맵게

import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    scovilleTemp, scovilleTemp2, time = 0, 0, 0
    
    if K == 0 or scoville[1] == 0:
        answer = -1
    
    while answer == 0:
        scoville.sort()
        if scoville[0] < K:
            scovilleTemp = float(heapq.heappop(scoville))
            scovilleTemp2 = float(heapq.heappop(scoville))
            heapq.heappush(scoville, scovilleTemp + (scovilleTemp2 * 2))
            time += 1
        elif time == 0:
            answer = -1
        else:
            answer = time
        
    print(scoville)
    print(answer)            
    return answer

#scoville, K = [1, 2, 3, 9, 10, 12], 7	
scoville, K = [1, 1, 1], 2	

solution(scoville, K)

# 2