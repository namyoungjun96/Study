# 프로그래머스 dfs/bfs 3단계 단어 변환

from collections import deque

def solution(begin, target, words):
    answer = 0
    
    if target not in words:
        return 0
    
    visited = [False] * len(words)
    answer = bfs(begin, target, words, visited)
    print(answer)
    return answer

def bfs(begin, target, words, visited):
    count = 0
    stack = [(begin, 0)]
    while stack:
        cur, depth = stack.pop()
        if cur == target:
            return depth
        
        for i in range(len(words)):
            if visited[i] == True:
                continue
            cnt = 0
            for a,b in zip(cur, words[i]):
                print("a : ", a, "b : ", b)
                if a!=b:
                    cnt += 1
            if cnt == 1:
                visited[i] = True
                stack.append((words[i], depth+1))

begin, target, words = "hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]	
solution(begin, target, words)

# begin	target	words	return
# "hit"	"cog"	["hot", "dot", "dog", "lot", "log", "cog"]	4
# "hit"	"cog"	["hot", "dot", "dog", "lot", "log"]	0