def solution(brown, yellow):
    answer = []
    answer = [yellow+2, 3]
    
    if yellow+2 >= brown//2:
        answer[1] += 1
        answer[0] = answer[1]+2
    
    return answer

brown, yellow = 10, 2
solution(brown, yellow)

# brown yellow return
# 10	2	[4, 3]
# 8     1	[3, 3]
# 24	24	[8, 6]
# 12    4   [4, 4]