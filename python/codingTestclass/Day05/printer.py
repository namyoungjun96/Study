# 프로그래머스 스택/큐 2단계 프린터

def solution(priorities, location):
    answer = 0
    temp = []
    while len(temp) != len(priorities):
        answer = recursion(priorities, temp, answer)
        print(answer)
        temp.append(answer)

    return answer

def recursion(priorities, temp, start):
    if start == len(priorities):
        start = 0
    max = priorities[start]
    
    if max > priorities[start+1] and start not in temp:
        print("small")
        recursion(priorities, temp, start+1)
    elif max < priorities[start+1] and start not in temp:
        print("big")
        max = priorities[start+1]
        recursion(priorities, temp, start+1)
    else:
        print("return")
        return start

priorities,	location = [2, 1, 3, 2], 2
priorities2, location2 = [1, 1, 9, 1, 1, 1], 0

solution(priorities, location)