import sys

a, b = list(map(int, sys.stdin.readline().split()))
arr = []
count = 1
answer = 0

while count <= 1000:
    for i in range(count):
        arr.append(count)
        
    count += 1
    
print(sum(arr[a-1:b]))