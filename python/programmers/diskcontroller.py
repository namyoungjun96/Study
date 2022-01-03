# 프로그래머스 우선순위 큐 3단계 디스크 컨트롤러

import heapq

def solution(jobs):
    answer = 0
    count = 0
    time = []
    jobs.sort()
    time.append([jobs[0][1], jobs[0][0]])
    del jobs[0]
    
    for i in range(len(jobs)):
        temp = jobs[i][0]
        jobs[i][0] = jobs[i][1]
        jobs[i][1] = temp
    
    heapq.heapify(jobs)
    
    while jobs:
        jobsTemp = list(heapq.heappop(jobs))
        print(jobsTemp)
        time.append([jobsTemp[0] + time[count][0], jobsTemp[1]])
        count += 1
        
    for i in range(len(time)):
        answer += (time[i][0] - time[i][1])
    
    print(time)
    answer //= len(time)     
    print(answer)
    return answer

jobs = [[0, 3], [1, 9], [2, 6]]
solution(jobs)
# 9