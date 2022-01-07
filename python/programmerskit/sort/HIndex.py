# 프로그래머스 정렬 2단계 H-Index
# H-Index = 논문의 갯수가 인용수 만큼일때 ,, 먼말인지 잘 모르겠음
# 예를들어 6 5 4 1 0 이면 H-Index = 3
# 혹은 24 26 이면 H-Index = 2

def solution(citations):
    answer = 0
    citations.sort(reverse = True)
    
    for i in range(len(citations)):
        if i >= citations[i]:
            answer = i
            break
        
        answer = i+1
        
    print(answer)
    return answer

citations = [6, 5, 3, 1, 0]	
solution(citations)

# 3 | 6 5 3 1 0