# 백준 11399번 ATM

import sys

x = int(sys.stdin.readline())
people = list(map(int, input().split()))
people.sort()
time = [0] * x
answer = 0

for i in range(len(people)):
    for j in range(i+1):
        time[i] += people[j]
    answer += time[i]
        
print(answer)