# 프로그래머스 1단계 부족한 금액 계산하기

def solution(price, money, count):
    answer = -1
    sum = 0
    
    for i in range(1, count+1):
        sum += price * i
    answer = sum - money
    
    if answer < 0:
        answer = 0

    return answer