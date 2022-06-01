from collections import defaultdict

def solution(tickets):
    answer = []
    routes = defaultdict(list)
    tickets.sort(reverse=True)
    
    for i in tickets:
        routes[i[0]].append(i[1])
    
    print(routes)
    current_list = ["ICN"]
    
    while current_list:
        current = current_list[-1]
        print(current, routes, answer)
        if current in routes and routes[current]:
            current_list.append(routes[current].pop())
        else:
            answer.append(current_list.pop())
            
    answer.reverse()
    print(answer)
    return answer
    
# solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])
# solution([["ICN", "A"], ["ICN", "B"], ["B", "ICN"]])
solution([["ICN", "AOO"], ["AOO", "BOO"], ["BOO", "COO"], ["COO", "DOO"], ["DOO", "EOO"], ["EOO", "DOO"], ["DOO", "COO"], ["COO", "BOO"], ["BOO", "AOO"]])
# solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])

# tickets	return
# [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]	["ICN", "JFK", "HND", "IAD"]
# [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]	["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]