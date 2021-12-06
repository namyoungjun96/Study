from collections import deque

queue = deque([])

list1 = [1, 0, 0, 1]
queue.append(list1)
print(queue)
print(queue.popleft())