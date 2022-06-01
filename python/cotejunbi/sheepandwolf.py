from collections import defaultdict, deque

def solution(info, edges):
    answer = 0
    graph = defaultdict(list)
    
    for i in edges:
        graph[i[0]].append(i[1])
        # graph[i[1]].insert(0, i[0])
    print(graph)
    
    answer = bfs(0, 1, 0, graph, info)
    print(answer)
    return answer

# def bfs(cur, sheep, wolf, graph, info):
#     q = deque(graph[cur])
    
#     while q:
#         cur = q.popleft()
#         sheep += info[cur] ^ 1
#         wolf += info[cur]
#         print("cur", cur, "info", info[cur], "sheep", sheep, "wolf", wolf)
        
#         if info[cur] == 1 and cur not in graph:
#             sheep -= info[cur] ^ 1
#             wolf -= info[cur]
#         elif sheep > wolf:
#             q.extend(graph[cur])
#         else:
#             if cur in graph:
#                 q.append(cur)
#             sheep -= info[cur] ^ 1
#             wolf -= info[cur]
    
#     return sheep

def bfs(cur, sheep, wolf, graph, info):
    q = deque([graph[cur]])
    visited = [False] * len(info)
    visited[cur] = True
    
    while q:
        cur = q.popleft()
        
        for i in cur:
            visited[i] = True
            sheep += info[i] ^ 1
            wolf += info[i]
            print("cur", i, "info", info[i], "sheep", sheep, "wolf", wolf, "q", q)

            if sheep > wolf:
                q.append(graph[i])
            else:
                if i in graph:
                    visited[i] = False
                sheep -= info[i] ^ 1
                wolf -= info[i]
        break
    
    print(q)
    return sheep

solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]])
# solution([0,1,0,1,1,0,1,0,0,1,0], [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]])
# info	edges	result
# [0,0,1,1,1,0,1,0,1,0,1,1]	[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]	5
# [0,1,0,1,1,0,1,0,0,1,0]	[[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]	5