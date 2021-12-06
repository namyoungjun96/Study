# 프로그래머스 DFS 2단계 타겟넘버
# 코드를 참조함

def solution(numbers, target):
    n = len(numbers)
    answer = 0
    def dfs(index, result):
        if index == len(numbers):
            if result == target:
                nonlocal answer
                answer += 1
            return
        else:
            dfs(index+1, result+numbers[index])
            dfs(index+1, result-numbers[index])
    dfs(0,0)
    return answer


numbers, target = [1, 1, 1, 1, 1], 3

print(solution(numbers, target))

'''
-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3
'''