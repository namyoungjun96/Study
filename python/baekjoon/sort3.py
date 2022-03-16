# 백준 10989번 수 정렬하기 3
# 파이썬은 for문 안에서 append를 사용하게되면, 메모리 재할당이 이루어져
# 메모리를 효율적으로 사용하지 못한다. 입력값이 많을수록 재할당이 많아져
# 메모리 관리에 비효율적이기에, 미리 관리한 상태에서 메모리의 값만 바꾸는
# 방식을 썼다고 한다.. * 파이썬 메모리는 잘 몰라 답 봤음

import sys

n = int(sys.stdin.readline())
numericList = [0] * 10001

for i in range(n):
    numericList[int(sys.stdin.readline())] += 1
    
for i in range(10001):
    if numericList[i] != 0:
        for j in range(numericList[i]):
            print(i)