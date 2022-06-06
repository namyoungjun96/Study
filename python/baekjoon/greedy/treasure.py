import sys

length = int(input())
arrA = list(map(int, sys.stdin.readline().split()))
arrB = list(map(int, sys.stdin.readline().split()))
arrA.sort(reverse=True)
temp = sorted(arrB)
answer = 0

for i in range(length):
    answer += arrB[arrB.index(temp[i])] * arrA[i]

print(answer)