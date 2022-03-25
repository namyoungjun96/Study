def solution(n):
    answer = 0
    temp = bin(n)
    num = n + 1
    
    while answer == 0:
        bigtemp = bin(num)
        if n < num and temp.count('1') == bigtemp.count('1'):
            answer = num
        else:
            num += 1
    
    return answer