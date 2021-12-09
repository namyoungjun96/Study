# 프로그래머스 스택/큐 2단계 주식가격
# 효율성 검사 불통과...

def solution(prices):
    answer = []

    for i in range(len(prices)-1):
        answer.append(recursion(prices, i, i, 0))
    
    answer.append(0)
    return answer

def recursion(prices, stock, count, time):
    if count < len(prices)-1 and prices[stock] <= prices[count]:
        return recursion(prices, stock, count+1, time+1)
    
    else:
        return time

prices = [1, 2, 3, 2, 3]
#return = [4, 3, 1, 1, 0]
solution(prices)