# 프로그래머스 카카오 2021 블라인드 채용 1단계 실패율
# 1시간 다른 사람의 답을 참고함
# count함수의 이해...
# count는 리스트 혹은 문자열에 있는 .count(?)의 개수를 찾아낸다.

def solution(N, stages):
    answer = {}
    denominator = len(stages)
    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stage)
            answer[stage] = count / denominator
            denominator -= count
        else:
            answer[stage] = 0
    answer = sorted(answer, key=lambda x : answer[x], reverse=True)
    return answer