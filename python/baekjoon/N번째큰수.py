import sys

t = int(input())
answer = []

for i in range(t):
    arr = list(map(int, sys.stdin.readline().split()))
    
    arr.sort()
    answer.append(arr[7])
    
for i in answer:
    print(i)