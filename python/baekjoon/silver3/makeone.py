# 백준 1463번 1로 만들기
# 점화식을 도저히 못만들겠다. 다음에 다시 도전하기

import sys

x = int(sys.stdin.readline())
answer = [0] * x

def make(num, count):
    if num == 1:
        answer[count] = 1
    if num % 3 == 0:
        make(num//3, count + 1)
    elif num > 1:
        make(num-1, count + 1)
    if num % 2 == 0:
        make(num//2, count + 1)
    elif num > 1:
        make(num-1, count + 1)
        
make(x, 0)
for i in range(len(answer)):
    if answer[i] == 1:
        print(i)
        break