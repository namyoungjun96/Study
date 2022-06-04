# meetroom = {1: 4, 3: 5, 0: 6, 5: 7, 6: 10, 8: 11, 2: 13, 12: 14}
# meetlist = [0, 1, 2, 3, 5, 6, 8, 12]
# answer = 0

# 실패
# 다시 풀어본다 쉬박..

import sys

meetcount = int(sys.stdin.readline())
meetroom = {}
answer = 0

for i in range(meetcount):
    start, end = map(int, sys.stdin.readline().split())
    
    if start not in meetroom:
        meetroom[start] = end
    else:
        if end < meetroom[start]:
            meetroom[start] = end

sorted(meetroom.items(), key=lambda x: x[1])

end = list(meetroom.keys())[0]

for i in meetroom:
    if i >= end:
        answer += 1
        end = meetroom[i]

print(answer)

# for i in range(len(meetlist)//2 + 1):
#     time = meetroom[meetlist[i]]
#     count = 1
    
#     while time <= meetlist[-1]:
#         if time not in meetlist:
#             time += 1
#         else:
#             time = meetroom[time]
#             count += 1
            
#     answer = max(answer, count)

# for i in range(len(meetlist)//2 + 1):
#     time = meetroom[meetlist[i]]
#     if time in meetlist:
#         temp = meetlist[meetlist.index(time):]
#     else:
#         while time not in meetlist and time < meetlist[-1]:
#             time += 1
#         if time <= meetlist[-1]:
#             temp = meetlist[meetlist.index(time):]
#     count = 1
    
#     print(temp)
    
#     for j in temp:
#         if time <= j:
#             time = meetroom[j]
#             count += 1
    
#     answer = max(answer, count)

# meetroom = {1: 4, 3: 5, 0: 6, 5: 7, 6: 10, 8: 11, 2: 13, 12: 14}
# meetlist = [0, 1, 2, 3, 5, 6, 8, 12]