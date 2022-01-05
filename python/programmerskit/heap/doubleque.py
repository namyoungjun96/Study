# 프로그래머스 우선순위 큐 3단계 이중우선순위큐

import heapq

def solution(operations):
    answer = []
    heap = []
    
    while operations:
        command = operations.pop(0)
        
        if command[0] == 'I':
            heapq.heappush(heap, int(command[2:]))
        elif heap and command == "D 1":
            heap = heapq.nlargest(len(heap), heap)[1:]
            heapq.heapify(heap)
        elif heap and command == "D -1":
            heapq.heappop(heap)
        heap.sort()
        print(heap)
                    
    if len(heap) > 1:
        answer.append(heap[len(heap)-1]) 
        answer.append(heapq.heappop(heap))
    elif heap:
        answer.append(heapq.heappop(heap))
        answer.append(0)
    else:
        answer = [0, 0]
        
    print(answer)        
    return answer

operations = ["I 6", "I 2", "I 1", "I 4", "I 5", "I 3", "D 1", "I 7", "D -1", "I 6", "D -1", "D -1"]
solution(operations)

# ["I 16","D 1"], [0, 0]
# ["I 7","I 5","I -5","D -1"], [7,5]