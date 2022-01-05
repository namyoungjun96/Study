# DAY 07 문제풀이

def solution(prices):
    answer = []
    prices.pop()
    prices.reverse()
    
    while prices:
        time = 1
        compareNumber = prices.pop()
        
        for i in range(len(prices)-1, -1, -1):
            if compareNumber <= prices[i]:
                time += 1
            else : 
                break
        
        answer.append(time)
    
    answer.append(0)
    return answer

prices = [1, 2, 3, 2, 3]
#return = [4, 3, 1, 1, 0]
solution(prices)

# [3, 2, 3, 2, 1]