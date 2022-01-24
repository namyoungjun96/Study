# 프로그래머스 카카오 2020 인턴십 키패드 누르기
# 풀이는 카카오 Tech를 참고했다. 격자에 대한 생각을 전혀 못해 다시한번 핸들링을 어떻게 해야 하는지 알게 해주었다.
# 푸는건 30분 걸렸다.

def solution(numbers, hand):
    answer = ''
    numbers.reverse()
    
    graph = [[3,1],[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
    left = [3, 0]
    right = [3, 2]
    
    while numbers:
        num = numbers.pop()
        if num == 1 or num == 4 or num == 7:
            left = graph[num]
            answer += "L"
        elif num == 3 or num == 6 or num == 9:
            right = graph[num]
            answer += "R"
        elif abs(left[0] - graph[num][0]) + abs(left[1] - graph[num][1]) == abs(right[0] - graph[num][0]) + abs(right[1] - graph[num][1]) and hand == "left" :
            left = graph[num]
            answer += "L"
        elif abs(left[0] - graph[num][0]) + abs(left[1] - graph[num][1]) == abs(right[0] - graph[num][0]) + abs(right[1] - graph[num][1]) and hand == "right" :
            right = graph[num]
            answer += "R"
        elif abs(left[0] - graph[num][0]) + abs(left[1] - graph[num][1]) > abs(right[0] - graph[num][0]) + abs(right[1] - graph[num][1]):
            right = graph[num]
            answer += "R"
        else:
            left = graph[num]
            answer += "L"
    
    return answer