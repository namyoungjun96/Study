# import sys

# N = int(sys.stdin.readline())

# time = [[0]*2 for _ in range(N)]
# for i in range(N):
#     s, e = map(int, sys.stdin.readline().split())
#     time[i][0] = s
#     time[i][1] = e

# time.sort(key = lambda x: (x[1], x[0]))

# print(time)

# cnt = 1
# end_time = time[0][1]
# for i in range(1, N):
#     if time[i][0] >= end_time:
#         print(time[i][0])
#         cnt += 1
#         end_time = time[i][1]

# print(cnt)

meetroom = {1: 4, 3: 5, 0: 6, 5: 7, 6: 10, 8: 11, 2: 13, 12: 14}
meetlist = [0, 1, 2, 3, 5, 6, 8, 12]
answer = 0

import sys

# meetcount = int(sys.stdin.readline())
# meetroom = {}
# answer = 0

# for i in range(meetcount):
#     start, end = map(int, sys.stdin.readline().split())
    
#     if start not in meetroom:
#         meetroom[start] = end
#         meetlist.append(start)
#     else:
#         if end < meetroom[start]:
#             meetroom[start] = end

sorted(meetroom.items(), key=lambda x: x[1])
end = list(meetroom.keys())[0]

for i in meetroom:
    if i >= end:
        answer += 1
        end = meetroom[i]

print(answer)