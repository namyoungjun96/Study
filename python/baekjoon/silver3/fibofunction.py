# 백준 1003 피보나치 함수
# DP는 나중에..

import sys

x = int(sys.stdin.readline())
testcase = [0] * x
answer = [0, 0]

for i in range(x):
    testcase[i] = int(sys.stdin.readline())
    
def fibonacci(num):
    if num == 0:
        answer[0] += 1
        return 0
    elif num == 1:
        answer[1] += 1
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)
    
for i in range(x):
    fibonacci(testcase[i])
    print(answer[0], answer[1])
    answer = [0, 0]