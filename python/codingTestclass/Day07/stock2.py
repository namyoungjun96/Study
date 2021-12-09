def solution(prices):
    answer = []
    time = 0
    lastTime = -1

    for i in range(len(prices)-1, -1, -1):
        print("i", i, "time", time)
        if prices[i] > prices[i-1]:
            answer.append(time)
        else:
            answer.append(time-lastTime)
        time += 1
        lastTime += 1

    answer.reverse()
    print(answer)
    return answer

prices = [1, 2, 3, 2, 3]
#return = [4, 3, 1, 1, 0]
solution(prices)