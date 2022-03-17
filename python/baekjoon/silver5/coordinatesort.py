import sys

n = int(sys.stdin.readline())
coordinate = []

for i in range(n):
    num1, num2 = map(int, sys.stdin.readline().split())
    coordinate.append([num1, num2])
    
coordinate.sort()

for i in range(n):
    print(coordinate[i][0], coordinate[i][1])