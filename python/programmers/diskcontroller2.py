# 프로그래머스 우선순위 큐 3단계 디스크 컨트롤러
# 이틀동안 고민

import heapq

def solution(jobs):
    answer = 0
    count = len(jobs)
    heap = []
    jobsTime = 0
    jobs.sort()
    time = jobs[0][1]
    answer = jobs[0][1]
    del jobs[0]
    
    while jobs or heap:
        if jobs and time >= jobs[0][0]:
            heapq.heappush(heap, [jobs[0][1], jobs[0][0]])
            jobs.pop(0)  

        if heap and heap[0][0] == jobsTime:
            temp = heapq.heappop(heap)
            print("job : ", jobsTime)
            jobsTime = 1
            answer += time - temp[1]
            time += 1
            print("answer : ", answer, "time : ", time)
        elif heap:
            jobsTime += 1
            time += 1
        else:
            time += 1
    
    answer //= count 
    print(answer)
    return answer

jobs = [[0, 3], [1, 9], [2, 6]]
solution(jobs)
# 9