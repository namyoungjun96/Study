# 프로그래머스 우선순위 큐 2단계 더 맵게

import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        if len(scoville) > 1:
            scovilleTemp = float(heapq.heappop(scoville))
            scovilleTemp2 = float(heapq.heappop(scoville))
            heapq.heappush(scoville, scovilleTemp + (scovilleTemp2 * 2))
            answer += 1
        else:
            return -1
                
    return answer

scoville, K = [1, 1, 1], 2	

solution(scoville, K)