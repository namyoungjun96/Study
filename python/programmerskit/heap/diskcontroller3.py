# 프로그래머스 우선순위 큐 3단계 디스크 컨트롤러
# 30분 생각 컷

import heapq

def solution(jobs):
    answer = 0
    divide = len(jobs)
    jobs.sort(reverse = True)
    time = 0
    heap = []
    
    while jobs or heap:
        if jobs and time >= jobs[len(jobs)-1][0]:
            heapq.heappush(heap, [jobs[len(jobs)-1][1], jobs[len(jobs)-1][0]])
            jobs.pop()
        elif heap:
            time += heap[0][0]
            answer += time - heap[0][1]
            heapq.heappop(heap)
        else:
            print("insert time")
            time = jobs[len(jobs)-1][0]
    
    answer //= divide
    print(answer)
    return answer

jobs = [[0, 3], [1, 9], [2, 6], [20, 3]]
solution(jobs)
# 9