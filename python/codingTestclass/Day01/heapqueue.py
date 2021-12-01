import heapq

heap=[]

heapq.heappush(heap, 50)
print(heap)

heapq.heappush(heap, 10)
print(heap)

heapq.heappush(heap, 20)
print(heap)

heapq.heappop(heap)
print(heap)

heapq.heappop(heap)
print(heap)

heapq.heappop(heap)
print(heap)

heap = [50, 10, 20]
print(type(heap))
res=heapq.heappop(heap)
print(heap)
heap = [50, 10, 20]
heapq.heapify(heap)
res=heapq.heappop(heap)
print(heap)

print('========================')

### 힙은 큐에 속해있으며, 우선순위를 정하는 특이한 경우이다.
### 우선순위를 정하는데에는 숫자가 높을수록 우선순위가 클 수도 있고, 숫자가 낮을수록 우선순위가 클 수도 있다.
### 그냥 heapq로 pop을 할 경우 우선순위가 없이 나가지만, heapify로 힙으로 만들고 나서 pop할 경우 우선순위대로 나간다.
### ***heap은 무조건 최소 힙

heap_contents = [1, 3, 5, 7, 9]
max_heap = []
for i in heap_contents:
    heapq.heappush(max_heap, i)
print(max_heap)
res=heapq.heappop(max_heap)
print(res, max_heap)

print('========================')

heap_contents = [1, 3, 5, 7, 9]
max_heap = []
for i in heap_contents:
    heapq.heappush(max_heap, [-i, i])
print(max_heap)
res=heapq.heappop(max_heap)
print(res[1], max_heap)