# 백준 1920번 수 찾기
# 시간복잡도..?
# 푸는중. 이진탐색으로.

import sys

n = int(sys.stdin.readline())
nlist = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
mlist = list(map(int, sys.stdin.readline().split()))
answer = [0] * m
nlist.sort()

# for i in range(m):
#     for j in range(len(nlist)):
#         if mlist[i] == nlist[j]:
#             del nlist[j]
#             answer[i] += 1
#             break

def find(temp, nlist, start, mlist):
    if mlist[start] == nlist[temp]:
        del nlist[temp]
        answer[start] = 1
    elif temp < len(nlist)-1:
        find(temp + 1, nlist, start, mlist)
        
for i in range(m):
    find(0, nlist, i, mlist)

for i in range(len(answer)):
    print(answer[i])