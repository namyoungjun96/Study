# 프로그래머스 정렬 2단계 가장 큰 수
# 문자열로 바꾸면 사전순으로 정렬된다는것을 모름,, 그래서 답을 봐버림..
# * 파이썬에 대한 기본적인 이해도가 딸리는듯

def solution(numbers):
    answer = ''
    
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x: x*3, reverse=True)
    answer = str(int(''.join(numbers)))
    
    print(answer)
    return answer

numbers = [6, 10, 2]
solution(numbers)

# [6, 10, 2] "6210"
# [3, 30, 34, 5, 9] "9534330"