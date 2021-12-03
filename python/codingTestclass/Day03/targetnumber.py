# 프로그래머스 DFS 2단계 타겟넘버

def solution(numbers, target):
    answer = 0

    for i in numbers:
        i

numbers, target = [1, 1, 1, 1, 1], 3

answer = solution(numbers, target)
print(answer)

'''
-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3
'''