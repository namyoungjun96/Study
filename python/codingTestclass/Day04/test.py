a=[1, 2, 3, 3]

from collections import deque

queue = deque([a])
print(queue)

queue = deque([])
for i in range(len(a)):
    queue.append(a[i])
temp = queue.popleft()
print(temp)

print(max(queue))
print(queue)
print(queue[0])

a=[10, 2, 3, 4, 5]
print(a[0][0])