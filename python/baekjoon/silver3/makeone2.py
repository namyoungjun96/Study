import sys

x = int(sys.stdin.readline())
answer = [0] * x
answer[1] = 1
answer[2] = 1
answer[3] = 1

def make(num, count):
    print("answer[num] :", answer[num], "| num :", num)
    if num % 3 == 0 and answer[num] == 0:
        answer[num] += make(num//3, count)
    elif num > 1 and answer[num] == 0:
        answer[num] += make(num-1, count)
    if num % 2 == 0 and answer[num] == 0:
        answer[num] += make(num//2, count)
    elif num > 1 and answer[num] == 0:
        answer[num] += make(num-1, count)
    return answer[num]
        
make(x-1, 0)

print(answer)